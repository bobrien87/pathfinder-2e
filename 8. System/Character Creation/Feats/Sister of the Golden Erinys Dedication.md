---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sister Of The Golden Erinys|Sister Of The Golden Erinys]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're from Isger or a member of the Sisterhood of the Golden Erinys.

The fighting style of the Sisterhood of the Golden Erinys is rooted in their understanding of devils. You gain the [[Additional Lore]] general feat for Devil Lore. When you choose this feat, you can choose to become sanctified as unholy.

You gain access to the asp coil. You have familiarity with the [[Asp Coil]] and [[Scourge]], treating them as simple weapons for the purposes of proficiency. If you're unholy, your Strikes using those weapons and your unarmed Strikes gain the unholy trait.

Special If you have the [[Monastic Weaponry]] feat, the asp coil gains the monk trait for you.

Sister of the Golden Erinys

**Source:** `= this.source` (`= this.source-type`)
