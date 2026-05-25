---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Lion Blade|Lion Blade]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Incapacitation]]"]
prerequisites: "Lion Blade Dedication"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You must be undetected by the target creature.

You quickly move in to bring your foe down with a single blow. You move up to your Speed then make a melee Strike. If you hit and deal damage, your foe must attempt a [[Fortitude]] save against your class DC or spell DC, whichever is higher. Regardless of the save outcome, the creature then becomes immune to your Stunning Surprise for 24 hours.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Stunned]] 1 and can't use reactions until its next turn.
- **Failure** The creature is [[Stunned]] 3 and can't use reactions until its next turn.
- **Critical Failure** The creature falls [[Unconscious]] for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
