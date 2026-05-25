---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Snarecrafter|Snarecrafter]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Magical Crafting, Snarecrafter Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've trained with the Brastlewark gnomes or studied their teachings, and learned the art of crafting their more magical snares. You learn the formulas for crafting the pit illusion snare and the shadow cloak snare or two uncommon magical snares of your level or lower that you have access to. When you set a magical snare, the DC of any saving throw it requires uses your spell DC if that's higher. When you craft a non-magical snare, you can choose to give it the magical trait. When you do so and the snare is one that normally deals damage, it deals an additional amount of force damage equal to its level.

**Source:** `= this.source` (`= this.source-type`)
