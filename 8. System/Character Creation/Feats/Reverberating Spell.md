---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Elementalist|Elementalist]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Metal]]", "[[Spellshape]]"]
prerequisites: "Elementalist Dedication, metal is in your elemental philosophy"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your spell disorients your targets with a metallic clangor. If the next action you use this turn is to Cast a non-cantrip Spell that deals damage in an area (such as a burst, line, or cone), the spell deals an additional 1d8 sonic damage and all creatures who fail their save against the spell are [[Deafened]] for 1 round. Targets who critically fail their saves against this spell are instead deafened for 1 minute. The spell gains the sonic trait.

**Source:** `= this.source` (`= this.source-type`)
