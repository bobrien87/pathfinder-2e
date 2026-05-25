---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Gnome]]", "[[Move]]", "[[Teleportation]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You must be adjacent to a living creature.

You phase through a space that a living creature occupies in a flash, spontaneously appearing on the opposite side of it in a vibrant display of colorful light. You move from your current location to another location that's still adjacent to the same living creature, but on the opposite side or corner of the creature's space. To determine whether a position is valid, use the same rules as for flanking: a line through the center of the two spaces must pass through opposite sides or corners of the creature's space.

You pass through the creature's life force, appearing in the selected location; this doesn't trigger reactions based on movement. You must be able to see your destination, and you can't move farther than your Speed would allow.

**Source:** `= this.source` (`= this.source-type`)
