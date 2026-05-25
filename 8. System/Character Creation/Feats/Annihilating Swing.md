---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Barbarian]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have embraced brute destructive power. You make a melee Strike that ignores any resistances the target has. If you target a solid unattended object or surface with your Strike, you might automatically destroy it without an attack roll. If you target any object or surface with Hardness 20 or less that isn't a magic item or the effect of a spell, you destroy it.

If the target object or surface is a magic item or the effect of a spell, you attempt to counteract it using your attack bonus with the Strike for the counteract check. Your counteract rank is 10th. On a successful counteract check, you destroy the object or surface unless it has Hardness greater than 20, in an artifact, or is similarly difficult to destroy.

You destroy up to a 5-foot cube of an object or surface larger than Medium.

**Source:** `= this.source` (`= this.source-type`)
