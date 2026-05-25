---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wildspell|Wildspell]]"
source-type: "Remaster"
level: "16"
traits: ["[[Concentrate]]", "[[Light]]", "[[Mythic]]", "[[Spellshape]]", "[[Visual]]"]
prerequisites: "Wildspell Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your [[Spellsurge]] aura is active.

You release a torrent of magic to fill the air with tiny, distracting explosions of light. All creatures within your *spellsurge* aura become [[Concealed]], and all creatures outside the aura are concealed to creatures within it. However, you can ignore this concealment. This effect lasts until the end of your next turn, but you can extend the duration for an additional round by Sustaining it once per round.

**Source:** `= this.source` (`= this.source-type`)
