---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Animist]]", "[[Apparition]]", "[[Divine]]", "[[Stance]]", "[[Wandering]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You feed excess magical power into your apparition, allowing it to grow ethereal limbs it can use to help shape and focus your spells. Once per turn while in this stance, you can use a spellshape feat that normally requires one action as a free action instead, but only to affect spells that deal spirit, vitality, or void damage. This doesn't allow you to avoid or bypass any other restrictions or limitations normally associated with the spellshape feat.

**Source:** `= this.source` (`= this.source-type`)
