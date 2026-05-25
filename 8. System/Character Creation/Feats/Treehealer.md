---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Elf]]", "[[Exploration]]", "[[Healing]]", "[[Primal]]"]
frequency: "once per day"
source: "Pathfinder #210: Whispers in the Dirt"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You can undo the effect of demonic corruption in plants. By spending 10 minutes in contact with a tree that's been corrupted by demonic presence, you can restore the tree to its original health. This does not prevent that tree from becoming corrupted again in the future. Alternatively, you can spend 10 minutes in contact with a creature with the plant trait. At the end of this time, you restore @Damage[(7d8+56)[healing]] Hit Points to that creature and heal half that amount of your own Hit Points. Additionally, you can attempt to counteract any one curse or disease afflicting that plant creature as if you had cast [[Cleanse Affliction]] heightened to 7th rank. Your counteract rank for this is 7, and your counteract check is equal to your Will save or your spell attack modifier, whichever is higher.

**Source:** `= this.source` (`= this.source-type`)
