---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Unexpected Sharpshooter|Unexpected Sharpshooter]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Unexpected Sharpshooter Dedication, trained in Deception"
frequency: "once per PT1H"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Requirements** Your previous action was a ranged weapon Strike that missed a foe within 60 feet.

Somehow your stray bullet causes an unintended reaction that creates a problem for your enemy: perhaps a ricochet knocks your foe's weapon away or they stumble over stray debris in an attempt to dodge your bullets. Roll a Deception check to attempt to [[Shove]] `act shove statistic=deception`, [[Trip]] (`act trip statistic=deception`), or [[Disarm]] (`act disarm statistic=deception`)the foe you missed.

**Source:** `= this.source` (`= this.source-type`)
