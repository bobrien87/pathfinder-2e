---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your limbs tense as you deliver a mighty swing. Make a melee Strike. If it hits, you deal an extra die of weapon damage and push the target back by 5 feet. If you're at least 10th level, increase this to two extra dice and push the target by 10 feet, and if you're at least 18th level, increase it to three extra dice and push the target by 15 feet.

**Awakening** On a critical hit, you push the target back double the normal distance and knock it [[Prone]].

**Awakening** On a hit, you deal 1d6 bleed damage. This increases to 2d6 at 10th level and 3d6 at 18th level.

**Source:** `= this.source` (`= this.source-type`)
