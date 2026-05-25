---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Monk]]", "[[Occult]]", "[[Water]]"]
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** A creature within your reach is [[Prone]] or swimming.

You summon the explosive power of a geyser beneath a foe. The required creature must attempt a [[Fortitude]] save against your class DC as elemental water confounds their senses; if the creature is prone, they can Stand as a free action.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Sickened]] 1.
- **Failure** The target is [[Sickened]] 2. If you have a free hand and they are not larger than you, you can attempt an Athletics check to [[Grapple]] them as a free action.
- **Critical Failure** As failure, but if you succeed at the Athletics check to Grapple them, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
