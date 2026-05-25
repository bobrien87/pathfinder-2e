---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Ratfolk]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your cheeks are stretchy, and you can store up to four items of light Bulk or less in these cheek pouches. None of these items can have a dimension longer than 1 foot. As long as you have at least one item in your cheek pouches, your speech is noticeably difficult to understand. Placing an item in your cheek pouch or retrieving one is an Interact action. You can empty your mouth with a single action, causing everything you had stored in your cheek pouches to fall to the ground in your square.

**Source:** `= this.source` (`= this.source-type`)
