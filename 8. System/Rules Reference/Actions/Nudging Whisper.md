---
type: action
source-type: "Remaster"
traits: ["[[Curse]]", "[[Divine]]", "[[Emotion]]", "[[Mental]]"]
cast: "Passive"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You lace your words with echoes of your ancestors' magic. If your next action is to [[Request]], you gain the effects of the [[Shameless Request]] feat, and if your next action is to [[Lie]], you gain the effects of the [[Confabulator]] feat. If you critically fail at either check, the target and anyone who witnessed you fail becomes immune to your Nudging Whisper for one day, though this doesn't necessarily let them know that you attempted to charm them.

**Source:** `= this.source` (`= this.source-type`)
