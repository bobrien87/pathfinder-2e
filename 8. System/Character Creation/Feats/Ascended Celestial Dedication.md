---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ascended Celestial|Ascended Celestial]]"
source-type: "Remaster"
level: "12"
traits: ["[[Destiny]]", "[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your Calling has driven you to perform mortal deeds that will result in your ascension to the ranks of celestials. You're headstrong and determined and hardly waver in your resolve; once per hour, you can roll twice and use the higher result on a Will saving throw. If you ever become [[Confused]], rather than attack wildly, you become stubbornly immobile, wasting all your actions until the condition ends.

Additionally, you emanate a nimbus of light. You shed bright light in a 30-foot radius (and dim light to the next 30 feet). You can suppress or reestablish this light as a single action that has the concentrate trait. As long as your nimbus is active, all allies in the area of your nimbus gain a +1 status bonus to saves against fear. You gain the [[Bless Ally]] action.

Ascended Celestial

**Source:** `= this.source` (`= this.source-type`)
