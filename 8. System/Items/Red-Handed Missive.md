---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Curse]]", "[[Magical]]", "[[Missive]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

Composed to look like an important document, a red-handed missive is a trap used by those who suspect someone has been going through their correspondence. If activated, the missive dissolves into red dye that coats anything touching the missive. Magic in the dye prevents it from washing off for 1 week.

**Source:** `= this.source` (`= this.source-type`)
