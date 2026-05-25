---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Fire]]", "[[Magical]]", "[[Versatile p]]"]
price: "{'gp': 2800}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking [[Flaming]] longsword* has an ornate brass hilt and a blade shaped like stylized flames. When wielded, the blade projects illumination resembling shimmering firelight, emitting dim light in a 10-foot radius.

**Activate—Shoot Fire** `pf2:2` (concentrate, manipulate)

**Effect** You cast the [[Ignition]] cantrip from the sword as a 7th-rank arcane spell, using your melee attack modifier with *searing blade* as your spell attack modifier.

**Source:** `= this.source` (`= this.source-type`)
