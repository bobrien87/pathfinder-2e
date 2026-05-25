---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Fan Dancer|Fan Dancer]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Incapacitation]]", "[[Visual]]"]
prerequisites: "Fan Dancer Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding two fans, one in each hand.

As you spin around and create wide arching circles with your fans, you manifest a mosaic of peonies that confuses your enemies. Stride twice and then attempt a Performance check against the Will DC of each creature you passed adjacent to.
- **Critical Success** The creature is [[Stunned]] 3 and [[Dazzled]] for as long as they're stunned.
- **Success** The creature is [[Stunned]] 1 and dazzled for 1 round.
- **Failure** The creature is dazzled for 1 round.
- **Critical Failure** The creature is unaffected and temporarily immune to further uses of Peony's Flourish for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
