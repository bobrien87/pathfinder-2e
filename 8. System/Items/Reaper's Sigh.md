---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Deadly d10]]", "[[Magical]]", "[[Relic]]", "[[Trip]]", "[[Wood]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 wounding striking scythe* is a weapon of intricately embellished blackened metals and polished surfaces. It was originally intended to venerate Urgathoa in her role as the herald of autumn in pre-Taldor Isger but has recently found more malevolent meaning. With the scythe in her hands, Urgathoa was said to cull the harvest for feast to usher in the cold, bleak winters. As Urgathoa's legends took a darker tone, the scythe's own legend was reclaimed to venerate Erastil and Pharasma as part of the holiday for which it now claims a name.

**Source:** `= this.source` (`= this.source-type`)
