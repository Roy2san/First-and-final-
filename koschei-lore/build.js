// Собирает src/*.js (module.exports = [...]) в data/*.json и проверяет ссылки.
// Запуск: node koschei-lore/build.js
const fs = require("fs");
const path = require("path");

const root = __dirname;
const srcDir = path.join(root, "src");
const outDir = path.join(root, "data");
fs.mkdirSync(outDir, { recursive: true });

const BIOMES = ["pogost", "les", "top", "omut", "med", "serebro", "zoloto", "smorodina", "nav", "buyan",
  "pole", "iriy", "kitezh", "lysaya", "peklo", "rahmany", "raspute"];
const FORMS = ["medved", "volk", "sokol", "shchuka", "mysh", "tur", "gornostay", "muravey", "voron", "uzh",
  "lyagushka", "lebed", "kon", "kozlenok"];
const SRC = ["folk", "lit", "recon", "game"];
const STANCE = ["ally", "neutral", "foe"];

let problems = 0;
const warn = (f, msg) => { problems++; console.log(`  ! ${f}: ${msg}`); };

const files = fs.readdirSync(srcDir).filter(f => f.endsWith(".js")).sort();
const counts = {};
for (const f of files) {
  const full = path.join(srcDir, f);
  delete require.cache[require.resolve(full)];
  let data;
  try { data = require(full); }
  catch (e) { warn(f, "не парсится: " + e.message); continue; }
  if (!Array.isArray(data)) { warn(f, "экспорт должен быть массивом"); continue; }
  const ids = new Set();
  data.forEach((d, i) => {
    const where = `${f}[${i}] ${d && (d.id || d.name) || ""}`;
    if (!d || typeof d !== "object") { warn(where, "не объект"); return; }
    if (d.id) { if (ids.has(d.id)) warn(where, "повтор id"); ids.add(d.id); }
    if (d.src && !SRC.includes(d.src)) warn(where, "src вне " + SRC.join("/"));
    if (d.stance && !STANCE.includes(d.stance)) warn(where, "stance вне " + STANCE.join("/"));
    for (const key of ["biomes", "where"]) {
      if (Array.isArray(d[key])) d[key].forEach(b => { if (!BIOMES.includes(b)) warn(where, `неизвестный биом «${b}»`); });
    }
    if (Array.isArray(d.forms)) d.forms.forEach(fm => { if (!FORMS.includes(fm)) warn(where, `неизвестный облик «${fm}»`); });
  });
  const name = f.replace(/\.js$/, "");
  fs.writeFileSync(path.join(outDir, name + ".json"), JSON.stringify(data));
  counts[name] = data.length;
}
console.log("Собрано:", Object.entries(counts).map(([k, v]) => `${k}=${v}`).join(", "));
console.log(problems ? `Замечаний: ${problems}` : "Замечаний нет");
