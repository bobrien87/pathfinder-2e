---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Exploration]]", "[[Mythic]]"]
cast: "Passive"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You focus your mind on your seat of power, then tap into this connection to transport yourself to its demiplane. This process takes 10 minutes. You can bring up to 10 willing creatures with you when you Enter Seat of Power; these creatures must remain within 30 feet of you for the duration of the activity.

You can remain in your seat of power for as long as you desire. Any creature that you bring to your seat of power in this way (including you) can depart the demiplane as a three-action activity that has the concentrate trait. They return to the location they were in when they Entered your Seat of Power, or the nearest unoccupied space if that location is occupied.

**Source:** `= this.source` (`= this.source-type`)
