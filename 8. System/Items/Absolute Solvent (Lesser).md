---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 21}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Originally formulated as a means of dissolving [[Everlasting Adhesive]], this powerful solvent can break almost any adhesive's grip. As absolute solvent is particularly effective against everlasting adhesive, it automatically dissolves everlasting adhesive. It attempts to counteract any other adhesives, such as Glue Bombs, at 3rd-rank and has a counteract modifier of +9.

**Source:** `= this.source` (`= this.source-type`)
