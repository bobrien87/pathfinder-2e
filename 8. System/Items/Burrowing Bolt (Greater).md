---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 650}"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** arrow, bolt

**Activate** `pf2:1` (manipulate)

These arrows have tips grooved like a drill bit and angled fletching, causing them to spin quickly about their shaft when fired. When striking a structure or object of Hardness 18 or less within your first range increment, an activated burrowing bolt tunnels into the surface silently and leaves a hole behind it, burrowing through up to 10 feet of material before magically vanishing.

**Source:** `= this.source` (`= this.source-type`)
