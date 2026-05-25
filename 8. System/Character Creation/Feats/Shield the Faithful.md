---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mortal Herald|Mortal Herald]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Aura]]", "[[Divine]]", "[[Sanctified]]"]
prerequisites: "Mortal Herald Dedication"
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You and those closest to you are protected by your deity's power. For 1 minute, you and all allies within 10 feet of you gain a +1 item bonus to AC and resistance 10 to spirit damage. In addition, when a creature adjacent to you hits you with a melee attack, or when a creature touches you or hits you with an unarmed attack, that creature takes @Damage[(ternary(gte(@actor.level,20),10,5))[spirit]] damage.

At 20th level, the spirit resistance increases to 15 and the spirit damage increases to 10.

**Source:** `= this.source` (`= this.source-type`)
