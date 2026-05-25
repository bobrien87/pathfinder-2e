---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Nagaji]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've trained to use unique nagaji eating habits to your advantage. By manipulating your throat muscles, you can create a pocket of air to store up to four items of light Bulk or less without risk of dissolving. None of these items can have a dimension longer than 1 foot.

As long as you have at least one item in your throat pocket, your speech is noticeably difficult to understand, and you have a visible bulge in your neck.

Placing an item in your throat pocket or retrieving one is an Interact action. You can empty your throat pocket with a single action, causing everything you had stored in it to fall to the ground in your square. Any item that was covered in dirt or grime comes out clean.

**Source:** `= this.source` (`= this.source-type`)
