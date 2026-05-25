---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wildspell|Wildspell]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Wildspell Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature Casts a Spell within your [[Spellsurge]] aura.

You absorb the scattered energy of others' failed spells, using it to recharge your own magic. You attempt to counteract the spell. If you're successful, you absorb the dispersed magical energy, regaining one spell or spell slot of 8th rank or lower of your choice. If you spend a Mythic Point when you successfully counteract the triggering creature's spell, you instead regain a 9th-rank spell or spell slot of your choice.

**Source:** `= this.source` (`= this.source-type`)
