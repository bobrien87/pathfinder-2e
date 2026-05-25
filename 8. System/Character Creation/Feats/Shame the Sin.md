---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Elf]]"]
frequency: "once per PT1H"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** You critically hit a demon with a Strike.

Your conviction against the sins that all demons grow from is so strong that you can force a demon to suffer from its sins when you strike a sound blow against them. In addition to doing the normal damage for your critical hit, the demon also suffers the effects of its special vulnerability. If the demon has no special vulnerability, it instead takes an additional @Damage[(ternary(gte(@actor.level,17),3,ternary(gte(@actor.level,13),2,1)))d6[mental]] damage. This increases to 2d6 mental damage at 13th level and to 3d6 mental damage at 17th level.

**Source:** `= this.source` (`= this.source-type`)
