---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sterling Dynamo|Sterling Dynamo]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Sterling Dynamo Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You lash out with a powerful punch, extending your dynamo to a greater length in order to attack two creatures in a row. Make a single bludgeoning or piercing dynamo Strike and compare the attack roll result to the ACs of up to two foes. The first foe must be within your melee reach and the second foe must be adjacent to the first foe in a straight line away from you. Roll damage only once and apply it to each creature you hit. A Piston Punch counts as two attacks for your multiple attack penalty. Reduce the operational time of your sterling dynamo by 1 hour.

**Source:** `= this.source` (`= this.source-type`)
