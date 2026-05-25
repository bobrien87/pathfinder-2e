---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 150}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This simple leather armor is adorned with a series of pockets and pouches, all within easy reach. Designed for a busy crafter, each pocket or pouch contains a specific tool required for specialized crafting.

**Activate—Find Tool** `pf2:1` (concentrate, manipulate)

**Frequency** once per hour

**Effect** You reach into a pouch or pocket and find the specific short or long tool you're looking for. The armor manifests the tool into existence for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
