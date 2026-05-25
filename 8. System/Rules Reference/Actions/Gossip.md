---
type: action
source-type: "Remaster"
traits: ["[[Downtime]]", "[[Secret]]"]
cast: "Passive"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You seek out rumors about the infiltration's target. Attempt a normal, hard, or very hard Diplomacy check.
- **Critical Success** You gain inside information about the location or group you're trying to infiltrate. This grants you a +2 circumstance bonus to future checks you attempt for preparation activities for this infiltration. If you share this information, those you share it with also gain this bonus.
- **Success** You gain inside information about the place or group you're attempting to infiltrate that aids your planning.
- **Failure** You learn nothing.
- **Critical Failure** You hear a few mistaken rumors and take a -2 circumstance penalty to your next check for a preparation activity. Word spreads around that you're asking after that group or individual, increasing your Awareness Points by 1.

**Source:** `= this.source` (`= this.source-type`)
