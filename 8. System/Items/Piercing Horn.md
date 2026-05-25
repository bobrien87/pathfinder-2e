---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 52}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A beast's horn or horns have been grafted onto your skull. You gain a horn unarmed attack that deals 1d8 piercing damage. This horn is in the brawling group.

**Source:** `= this.source` (`= this.source-type`)
