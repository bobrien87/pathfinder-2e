---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Kobold]]"]
prerequisites: "expert in Crafting, Snare Crafting"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

If the snare normally takes 1 minute to Craft, you can Craft it with 3 Interact actions instead. Each day during your daily preparations, you can prepare three snares from your formula book for quick deployment (increasing to four snares if you're a master in Crafting and five if you're legendary). Snares prepared in this way don't cost you any resources to Craft.

When a creature critically fails its saving throw against and takes damage from the initial effect of a snare you Crafted and deployed, that creature is [[Off Guard]] until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
