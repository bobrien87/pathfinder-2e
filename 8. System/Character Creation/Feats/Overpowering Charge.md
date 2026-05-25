---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Barbarian]]", "[[Fighter]]"]
prerequisites: "Barreling Charge"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You trample your foes as you charge past them. When you use [[Barreling Charge]] and successfully move through a creature's space, that creature takes @Damage[@actor.abilities.str.mod[bludgeoning]]{bludgeoning} damage equal to your Strength modifier. If you critically succeed, the creature takes double this amount of damage and becomes [[Off Guard]] until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
