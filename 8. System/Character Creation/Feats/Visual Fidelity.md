---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Inventor]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've found a way to use a hodgepodge combination of devices to enhance your visual abilities in every situation. You gain darkvision and low-light vision, and you can see [[Invisible]] creatures and objects as translucent shapes, though these shapes are indistinct enough to be [[Concealed]] to you.

If an effect would give you the [[Blinded]] condition, the effect must attempt a counteract check against your class DC, with your counteract rank equaling half your level, rounded up. On a failed counteract check, you aren't blinded-your various devices are able to compensate.

**Source:** `= this.source` (`= this.source-type`)
