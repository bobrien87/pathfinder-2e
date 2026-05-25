---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Werecreature|Werecreature]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Visual]]"]
prerequisites: "Werecreature Dedication, weretiger"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're in hybrid or tiger shape and your last action was a critically successful Strike with your unarmed attack.

You attack with a feline grace as captivatingly beautiful as it is deadly. All enemies within 30 feet of the creature you critically hit must attempt at a [[Will]] save against your class DC. Enemies that fail their saves become [[Frightened]] 1 and are [[Fascinated]] with you for 1 round. Your hostile actions don't end this fascination, but those of your allies do. Regardless of the effects of the save, the creature is immune to Fearful Symmetry for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
