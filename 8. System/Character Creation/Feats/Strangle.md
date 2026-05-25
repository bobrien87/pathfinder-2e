---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wrestler|Wrestler]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Wrestler Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a creature [[Grabbed]] or [[Restrained]].

You squeeze the breath out of your foe. Make an unarmed melee Strike against the creature you have [[Grabbed]] or [[Restrained]]. On a success, you gain a circumstance bonus to damage equal to the number of weapon damage dice, and the target can barely speak until the start of your next turn or until it Escapes, whichever comes first. While it can barely speak, the target can't vocalize above a hoarse whisper, and it must succeed at a DC 10 flat check or lose any action that requires speech. For an action requiring speech that is also a manipulate action, like [[Casting a Spell]] with the concentrate and manipulate trait, the target just rolls a single DC 10 flat check, rather than an additional DC 5 flat check for being grabbed.

> [!danger] Effect: Strangle

**Source:** `= this.source` (`= this.source-type`)
