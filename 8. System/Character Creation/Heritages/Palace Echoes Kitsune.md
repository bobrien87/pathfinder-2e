---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kitsune|Kitsune]]"
traits: ["[[Kitsune]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You descend from kitsune who possessed such compelling powers of persuasion that they could walk into a palace at sunrise and end up as the power behind the throne by nightfall. You gain the [[Nudging Whisper]] action.

Your alternate form is a common Medium humanoid ancestry prevalent where you grew up (typically human) called a tailless form.

**Source:** `= this.source` (`= this.source-type`)
