---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Catfolk]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a habit of always being in the way when other creatures attempt to move. Attempt an [[Acrobatics]] check against an adjacent creature's Reflex DC.

> [!danger] Effect: Catfolk Dance
- **Critical Success** The target creature gains a -2 circumstance penalty to Reflex saves and is [[Off Guard]] until the start of your next turn.
- **Success** The target creature gains a -2 circumstance penalty to Reflex saves until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
