---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Force]]", "[[Reincarnated]]"]
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Before your soul returned from death, you interacted with a host of other souls on their way to the Boneyard. One of these acquaintances owes you a favor. You can temporarily summon it to come to your aid, and it appears as a swirling mass of ectoplasm with indiscernible features and a translucent dagger, the favored weapon of Pharasma. This functions as [[Spiritual Guardian]] that you can cast once per day as a 9th-rank divine innate spell.

**Source:** `= this.source` (`= this.source-type`)
