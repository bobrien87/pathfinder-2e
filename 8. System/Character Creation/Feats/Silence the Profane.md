---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Avenger|Avenger]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Avenger Dedication or Vindicator Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature you can observe within reach of your deity's favored weapon casts a spell.

**Requirements** You are wielding your deity's favored weapon.

Your training included instruction on how to prevent enemy priests from using their magic against you, a technique you have mastered and adapted. Make a Strike with your deity's favored weapon against the triggering creature. On a success, the target is [[Off Guard]] until the end of your next turn. The triggering spell is disrupted on a critical success, or on a success if the target is your hunted prey and the spell is a divine spell.

**Special** If your deity's favored weapon is a ranged weapon, this reaction can trigger if the target is within its first range increment and you can make a ranged Strike instead of a melee Strike.

**Source:** `= this.source` (`= this.source-type`)
