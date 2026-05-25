---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Barbarian]]", "[[Incapacitation]]", "[[Rage]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A quick strike to the face or mouth silences your opponent. Make a melee Strike against an enemy. If it hits, the enemy must succeed at a [[Fortitude]] save against your class DC.
- **Success** The target is unaffected.
- **Failure** The target is dazed and can barely vocalize. It's [[Stunned]] 1 and its speech is raspy and hard to understand. It must succeed at a DC 11 flat check to use linguistic actions or Cast a Spell, unless the spell has the subtle trait.
- **Critical Failure** As failure, but the creature is [[Stunned]] 3 instead of stunned 1.

**Source:** `= this.source` (`= this.source-type`)
