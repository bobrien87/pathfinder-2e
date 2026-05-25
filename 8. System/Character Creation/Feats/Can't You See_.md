---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Druid]]", "[[Ranger]]"]
prerequisites: "trained in Occultism, expert in Stealth"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The eye rebels, the mind recoils—no matter how much those who can see you try to explain what's there, their friends' gazes just skitter over you, like a bird afraid to land. A character who attempts to Point Out your location must attempt a DC 14 flat check. If they fail, their allies misunderstand them and aren't sure where you are. On a critical failure, their allies think they pointed you out in a different location entirely, chosen by the GM. Similarly, when a creature critically fails to `act seek` you while you're [[Hidden]] to or [[Undetected]] by it, it thinks you're in a different location chosen by the GM. In either case, you appear to be hidden to a creature that thinks you're in a different location, though you're actually undetected by it for targeting and further uses of the Seek action.

**Source:** `= this.source` (`= this.source-type`)
