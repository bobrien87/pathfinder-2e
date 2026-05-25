---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Inventor]]"]
prerequisites: "construct innovation"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Aha! You lock on to your enemy's weak point to assist your construct companion in destroying it. When you Lock On, designate an enemy you can see. If your next action is to Command your construct, the construct gains a +2 circumstance bonus to attack rolls against the designated enemy until the end of the turn. If you use 2 actions for the Command, the bonus is instead a +3 circumstance bonus, or a +4 circumstance bonus if you're legendary in Crafting.

> [!danger] Effect: Lock On

**Source:** `= this.source` (`= this.source-type`)
