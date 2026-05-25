---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Agile]]", "[[Modular]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The polytool is a small metal rod with a number of simple tools folded inside. The user can extend a long ceramic blade, as well as an awl, chisel, file, flint and steel, hook, inkpen, magnifying glass, pliers, scissors, and a small saw. The flint and steel can be used up to 10 times before needing to be replaced. Though inspired by advanced Numerian technology, the polytool is a simple enough feat of metalworking that any blacksmith could produce it—perfect for the goddess [[Casandalee]] to spread innovation farther than actual Numerian tech could reach.

**Source:** `= this.source` (`= this.source-type`)
