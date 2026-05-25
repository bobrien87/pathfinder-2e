---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wylderheart|Wylderheart]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "member of the Wylderhearts, you're from Kyonin"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're from Kyonin.

You're primed to face off against threats from the Outer Rifts. You gain the [[Additional Lore]] skill feat for Demon Lore. If you were already trained in Demon Lore, you also become trained in a Lore skill of your choice. You gain a +1 circumstance bonus to initiative rolls in encounters against fiends, and if you tie with a fiend's initiative roll, you go first.

Certain wylderheart feats give you focus spells. When you gain your first wylderheart focus spell, you become trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for the wylderheart archetype spells is Wisdom, and they're primal spells. You can Refocus by celebrating life or spending time in nature.

Wylderheart

**Source:** `= this.source` (`= this.source-type`)
