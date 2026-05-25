---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Inventor]]"]
prerequisites: "Gadget Specialist"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are too brilliant to be caught off guard, and you always have just the right gadget for the situation. When you prepare your gadgets during your daily preparations, you can choose to leave one of them as a contingency gadget that you keep ready for just this situation, rather than declaring which gadget you're making. You can pull the contingency gadget out using an Interact action, at which point you must choose which gadget you had prepared as a contingency.

If you're legendary in Crafting, you can leave two contingency gadgets during your daily preparations, instead of just one.

**Source:** `= this.source` (`= this.source-type`)
