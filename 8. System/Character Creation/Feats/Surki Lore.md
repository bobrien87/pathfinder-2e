---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Surki]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Either through the tales of elders in your settlement or through the messages thumped by those who oversaw your generation dig, you hold the knowledge of many surkis before you. You become trained in Survival and the skill associated with the magical tradition from your magiphage ability (Arcana for arcane, Nature for primal, Occultism for occult, or Religion for divine). If you would automatically become trained in one of those skills (from your background or class, for example), you instead become trained in a skill of your choice.

You also gain the [[Additional Lore]] general feat for Surki Lore.

**Source:** `= this.source` (`= this.source-type`)
