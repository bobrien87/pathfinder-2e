---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Champion]]"]
prerequisites: "blessed swiftness"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The movement of you and your allies is swift and decisive as the judgment of your deity. If your ally starts a move action in your champion's aura, their movement during that action doesn't trigger reactions.

In addition, you're permanently [[Quickened]]. You can use your extra action only to Step or Stride. If you have a fly Speed, add Fly to this list. If you have an animal companion and are mounted on it at the start of your turn, you can have your mount be quickened that turn instead of you.

**Source:** `= this.source` (`= this.source-type`)
