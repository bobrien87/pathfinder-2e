---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Witch]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A broom is the only steed you need to fly through the night sky. During your daily preparations, you can anoint a single broom, staff, polearm, or similarly shaped object with a flying ointment made of special herbs and oils. Until the next time you make your daily preparations, it gains the magical trait, and you can ride on it while you're holding it with at least 1 hand. It moves at a fly Speed of 20 feet. The broom takes a –10-foot penalty to its Speed if laden with more than 20 Bulk, and crashes to the ground if it carries more than 30 Bulk. The broom can't be controlled by anyone but you. If you anoint a weapon or other held item, you can't ride the broom and wield it at the same time.

You can Craft your broomstick into a [[Flying Broomstick]] as though you had the formula for that item. If you anoint an item that's already a flying broomstick, the broom gains a +10-foot status bonus to its Speed and you can choose whether it works for anyone or only you.

**Source:** `= this.source` (`= this.source-type`)
