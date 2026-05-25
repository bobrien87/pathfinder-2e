---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 28}"
usage: "worn"
bulk: "—"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This badge depicting a hunting dog is used by Eutropia's supporters to indicate their allegiances.

**Activate—Bark** `pf2:2` (concentrate, manipulate, subtle)

**Frequency** once per hour

**Effect** The hunting dog makes a single bark that only you and a single target of your choice within 30 feet can hear. If the target is a supporter of Eutropia, you gain a +2 circumstance bonus to Diplomacy checks against them for the next minute.

> [!danger] Effect: Taldogis Badge

**Source:** `= this.source` (`= this.source-type`)
