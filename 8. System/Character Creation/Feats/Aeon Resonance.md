---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Runelord|Runelord]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Embed Aeon Stone"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You gain the resonant power of one embedded aeon stone as if it were placed in a [[Wayfinder]]. While you can embed multiple aeon stones in your flesh, you can gain the resonance power from only one embedded stone at a time, selected each day when you make your daily preparations.

**Special** At 8th level, you can take this feat again. If you do, you gain the resonance powers of up to four invested aeon stones instead of only one.

*PFS Note:* This feat acts as if an aeon stone was embedded in a *wayfinder*, and thus would not allow a second aeon stone to provide its resonance power from being embedded in a *wayfinder*.

**Source:** `= this.source` (`= this.source-type`)
