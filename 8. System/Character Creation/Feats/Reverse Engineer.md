---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Inventor]]"]
prerequisites: "trained in Crafting"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are incredibly skilled at reverse engineering items to learn their formulas or disassembling them just to disable them. If you are using the Critical Crafting alternate rules and you get a critical success on your Crafting check to reverse engineer an item, you can reassemble the original item with one of the critical success crafting benefits (as determined by your GM).

Furthermore, you can use Crafting instead of Thievery to `act disable-device skill=crafting` or `act pick-a-lock skill=crafting`.

**Source:** `= this.source` (`= this.source-type`)
