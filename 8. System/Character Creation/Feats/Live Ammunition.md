---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Artillerist|Artillerist]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Artillerist Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

There are generally few things as ill-advised as being shot out of a cannon or launched by a trebuchet, but people use the tactic every so often in a desperate situation. While it's more humane to use this strategy with mindless constructs or undead, occasionally an exceedingly foolhardy adventurer demands the opportunity to try it. Loading a creature requires two additional Load actions, which you must conduct personally. The creature must be willing, [[Unconscious]], or [[Restrained]] throughout the process, and the siege weapon must be physically capable of firing the creature in question, based on their size and shape. Typically, that means ballistae don't qualify, for example—nor do auto-catapults which require specifically-sized balls—but normal catapults and onagers work just fine. When you Launch the weapon, if the weapon usually targets an area, you target a single 5-foot square instead. The siege weapon deals its normal damage to its target, or to the modified area, and to the creature fired.

**Source:** `= this.source` (`= this.source-type`)
