---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Assassin|Assassin]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Assassin Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

All your Strikes against a creature you have [[Marked for Death]] have the death trait, causing the mark to be instantly killed when reduced to 0 Hit Points.

In addition, if the creature is killed this way, attempts to communicate with it, return it to life, turn it into an undead, or otherwise disturb its afterlife fail unless the effect's counteract rank is higher than half your level rounded up, or originates from an artifact or a deity. Use the level you were when you killed the creature, even if your level is higher at the time the attempt was made.

**Source:** `= this.source` (`= this.source-type`)
