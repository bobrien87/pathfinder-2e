---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Brandish]]", "[[Commander]]", "[[Emotion]]", "[[Flourish]]", "[[Mental]]", "[[Visual]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You wave your banner, inspiring allies to throw off the shackles of fear. Each ally currently benefiting from your commander's banner reduces their [[Frightened]] condition by 1 and can immediately attempt a new saving throw against any one mental effect currently affecting them. Regardless of the result, any ally that attempts this save is temporarily immune to Banner's Inspiration for 10 minutes.

*PFS Note:* This feat allows a new saving throw, so anything that happens on a failed save still occurs if a PC fails.

**Source:** `= this.source` (`= this.source-type`)
