---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Magical]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This coiled cord of brightly colored wire can be twisted neatly into any shape.

**Activate—Words on the Wind** `pf2:1` (concentrate)

**Frequency** once per 10 minutes

**Effect** You quietly mouth words to the wire, which sends them to a target with the effects of the [[Message]] cantrip.

**Source:** `= this.source` (`= this.source-type`)
