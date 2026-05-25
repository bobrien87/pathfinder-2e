---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Arcane]]", "[[Manipulate]]", "[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You inscribe a circle of arcane runes that dampen enemies' magic. You create a glowing magic circle in a @Template[burst|distance:5] within 30 feet. Creatures in the circle gain a +1 status bonus to saving throws against magic. The circle lasts until the end of your next turn, and you can Sustain it, to a maximum duration of 1 minute.

> [!danger] Effect: Spell Protection Array

**Source:** `= this.source` (`= this.source-type`)
