---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wildspell|Wildspell]]"
source-type: "Remaster"
level: "16"
traits: ["[[Concentrate]]", "[[Mythic]]"]
prerequisites: "Wildspell Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can break your spells down into raw magical potential and transfer it to an ally. Expend one prepared spell, spell slot, or Focus Point, and choose an adjacent ally or an ally within your [[Spellsurge]] aura. If you expended a spell or spell slot, the ally regains one expended spell or spell slot with a rank equal to or lower than the spell or spell slot you expended. If you expended a Focus Point, the ally regains a Focus Point. This feat can't grant more spell slots or Focus Points than the target can normally possess. You can't target yourself with this ability. Only one spell, spell slot, or Focus Point can be transferred with each use of this ability.

**Source:** `= this.source` (`= this.source-type`)
