---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You convert your mythic power into a magical effect. When you gain this feat, choose up to three spells of 1st or 2nd rank that take no more than 3 actions to cast and that are either instantaneous or have a duration of 10 minutes or less. You can spend a Mythic Point to cast any of those spells for their normal action cost and use mythic proficiency to determine your spell attack rolls and spell DCs, and the spells are automatically heightened to a rank equal to half your level (rounded up). If you don't normally have the ability to cast spells, you use Charisma as your spellcasting attribute modifier; otherwise, you use the spellcasting ability associated with your spellcasting class. You gain the Cast a Spell activity only for spells cast with this feat; you don't otherwise gain the typical benefits of being a spellcaster.

**Special** At 14th level, add one spell of 3rd rank for you to cast using this ability. At 20th level, add one 4th-rank spell.

**Source:** `= this.source` (`= this.source-type`)
