---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Wayang]]"]
prerequisites: "Inherit the Dreaming Heirloom"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The spirit within your pusaka resonates with other magical items in your possession. Your pusaka gains the following activation.

**Activate—Replenish Heirloom** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** Your pusaka uses its power to spark one of your depleted magic items to life. You Activate an Item you've invested even after you've used that activation the maximum number of times for its frequency. You can do so only if the item's level is half your level or lower, the activation has a frequency of once per day or more frequent, and you haven't already used the activation this round.

**Source:** `= this.source` (`= this.source-type`)
