// Собирает ../pixels.html: движок, облики и минимальные данные вшиваются в одну страницу.
// Запуск: node koschei-lore/px/build.js
const fs = require("fs");
const path = require("path");
const dir = __dirname;
const B = require("../src/bestiary.js");
const I = require("../src/items.js");
const SPECS = require("./specs.js");
const PX = require("./engine.js");

const missC = B.filter(b => !SPECS.creatures[b.id]).map(b => b.id);
const missI = I.filter(i => !SPECS.items[i.id]).map(i => i.id);
if (missC.length || missI.length) { console.log("Нет облика:", missC, missI); process.exit(1); }
B.forEach(b => PX.creature(SPECS.creatures[b.id], b.id));
I.forEach(i => PX.item(SPECS.items[i.id], i.id));

const data = {
  creatures: B.map(b => ({ id: b.id, name: b.name, stance: b.stance, kind: b.kind, origin: b.origin })),
  items: I.map(i => ({ id: i.id, name: i.name, type: i.type }))
};
const strip = s => s.replace(/if \(typeof module !== "undefined"\) module\.exports = [A-Z_]+;\s*$/m, "");
let html = fs.readFileSync(path.join(dir, "page.html"), "utf8");
html = html.replace("/*ENGINE*/", () => strip(fs.readFileSync(path.join(dir, "engine.js"), "utf8")))
  .replace("/*SPECS*/", () => strip(fs.readFileSync(path.join(dir, "specs.js"), "utf8")))
  .replace("/*DATA*/", () => JSON.stringify(data));
fs.writeFileSync(path.join(dir, "..", "pixels.html"), html);
console.log("pixels.html:", Math.round(html.length / 1024), "КБ;", B.length, "существ,", I.length, "предметов");
