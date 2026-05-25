---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Hobgoblin]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are trained to capture deserters, or "leeches." Make a melee Strike with weapon from the flail group. On a hit, the target takes a –10-foot status penalty to its Speed (or a –15-foot status penalty on a critical hit). The penalty lasts for 1 round. It applies only if the target has a land Speed and depends on legs or other targetable appendages to use its land Speed. As with all penalties to Speed, this can't reduce a creature's Speed below 5 feet.

> [!danger] Effect: Leech Clip

**Source:** `= this.source` (`= this.source-type`)
