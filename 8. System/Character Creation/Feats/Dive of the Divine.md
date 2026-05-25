---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Divine]]", "[[Sanctified]]"]
prerequisites: "Mortal Herald Dedication, fly Speed of at least 20 feet"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are at least 20 feet above the ground.

You dive from the sky, bringing down the might of the divine with you. You Fly straight down, landing safely in the nearest unoccupied space directly below you. When you land, all creatures in a @Template[type:emanation|distance:10] take @Damage[(ternary(gte(@actor.level,20),10,8))d10[spirit]|options:area-damage] damage (Type:fortitude check against the higher of your class DC or spell DC). On a failure, the target is pushed 5 feet (or 10 feet on a critical failure).

At 20th level, the spirit damage increases to 10d10.

**Source:** `= this.source` (`= this.source-type`)
