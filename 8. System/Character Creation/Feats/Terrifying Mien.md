---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Eternal Legend Dedication, master in Intimidation"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whether they have heard of your legend or seen your prowess on the field of battle, those already quaking in their boots grow weak when forced to stand against you. You gain resistance against bludgeoning, piercing, and slashing damage against Strikes made by creatures with the [[Frightened]] condition. This resistance is equal to four times the value of that creature's frightened condition.

> [!danger] Effect: Terrifying Mien

When this resistance applies to at least one of a creature's Strikes during their turn, that creature doesn't reduce the value of their frightened condition at the end of their turn.

**Source:** `= this.source` (`= this.source-type`)
