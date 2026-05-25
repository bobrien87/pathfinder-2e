---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Brace]]", "[[Orc]]", "[[Two hand d10]]", "[[Versatile p]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

As dwarves poured out of the Darklands following their Quest for Sky, the orcs driven before them adapted to their tactics—including dwarves' heavily armored infantry charges. Surviving orcs developed a response: a weapon that combines a spear and maul to crush heavy armor and skewer charging foes. Although rarely seen today, the weapon is remarkably effective in the right situation.

**Source:** `= this.source` (`= this.source-type`)
