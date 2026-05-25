---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Commander]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You gain the service of a young animal companion. You can affix your banner to your companion's saddle, barding, or a simple harness, determining the effects of your commander's banner and other abilities that use your banner from your companion's space, even if you are not currently riding your companion. A companion granted by this feat always counts as one of your squadmates and does not count against your maximum number of squadmates.

**Special** When you use Command an Animal to command the companion granted by this feat, it gains a reaction it can only use in response to your tactics. This reaction is lost if it is not used by the end of your turn.

**Source:** `= this.source` (`= this.source-type`)
