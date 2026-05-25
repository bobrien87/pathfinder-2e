---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Artillerist|Artillerist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Artillerist Dedication, Trained in crafting"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

It is a tradition among artillerists to name the siege weapon most important to them and closest to their heart—much as a sailor on a ship, the weapon is their livelihood. You've gone a step further, and you always make sure that your named artillery has the best possible maintenance and upkeep. You can spend a full day adjusting and working on a single siege weapon to designate it as your named artillery. The siege weapon you designated as your named artillery gains a +2 circumstance bonus to AC, Fortitude saves, and Reflex saves as well as additional Hit Points equal to twice your level.

During your daily preparations, you must spend at least one hour on maintenance to service your named artillery. If you fail to do so, or if you spend a full day designating a new piece of named artillery, the previous named artillery loses any benefits from this feat. Only one artillerist can designate a particular siege weapon as their named artillery, even if several artillerists are serving on the same siege weapon's crew (though it's typically more efficient for a group with several artillerists to divide them up, assigning one to each siege weapon).

**Source:** `= this.source` (`= this.source-type`)
