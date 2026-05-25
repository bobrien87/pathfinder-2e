---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wildspell|Wildspell]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]", "[[Sonic]]", "[[Spellshape]]"]
prerequisites: "Wildspell Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your [[Spellsurge]] aura is active.

Your magic explodes in bursts of excess energy, creating thunderous waves. If your next action is to Cast a Spell, attempt a DC 5 flat check.
- **Critical Success** Enemies within a @Template[burst|distance:10]{10-foot radius burst} centered on the target of the spell or within the spell's area of effect take @Damage[(2*@actor.level)[sonic]|options:area-damage]{sonic damage} equal to twice your level ([[Fortitude]] save saving throw against your class DC or spell DC, whichever is higher). Those who fail the save are also knocked [[Prone]].
- **Success** Enemies within a 10-foot radius burst centered on the target of the spell or within the spell's area of effect take @Damage[(@actor.level)[sonic]|options:area-damage]{sonic damage} equal to your level (basic Fortitude saving throw against your class DC or spell DC, whichever is higher). Those who critically fail the save are also knocked prone.
- **Failure** All creatures within a 10-foot radius burst centered on you take sonic damage equal to your level (basic Fortitude saving throw against your class DC or spell DC, whichever is higher). Those who fail the save are also knocked prone.

**Source:** `= this.source` (`= this.source-type`)
