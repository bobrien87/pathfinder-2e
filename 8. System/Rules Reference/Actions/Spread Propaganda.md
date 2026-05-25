---
type: action
source-type: "Remaster"
traits: ["[[Exploration]]", "[[Secret]]"]
cast: "Passive"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You spread propaganda about a faction (which may include an army, organization, or other particular group of people). This takes as long as it would normally take for you to Gather Information (typically 2 hours). At the end of this time, the GM rolls a secret Deception check to see how effective you were at spreading propaganda.
- **Critical Success** Your propaganda spreads effectively, and for the next month, creatures that succeed on checks to Gather Information learn your propaganda over facts about the subject. It cannot be traced back to you. You also learn information as if you succeeded at a [[Recall Knowledge]] check about the faction.
- **Success** As critical success, but the propaganda persists for 1 week and can be traced back to you by a character who critically succeeds at the skill check to Gather Information.
- **Failure** Your propaganda fails to take hold.
- **Critical Failure** Your propaganda is stunningly ineffective, and you take a –4 circumstance penalty to Deception checks to spread propaganda about the same subject for 1 week. In addition, the subject and its enemies become aware that you attempted to spread propaganda.

**Source:** `= this.source` (`= this.source-type`)
