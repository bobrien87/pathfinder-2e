---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** A creature is undetected by one or more of your allies but isn't undetected by you.

You indicate a creature that you can see to one or more allies, gesturing in a direction and describing the distance verbally. That creature is [[Hidden]] to your allies, rather than [[Undetected]]. This works only for allies who can see you and are in a position where they could potentially detect the target. If your allies can't hear or understand you, they must succeed at a Perception check against the creature's Stealth DC or they misunderstand and believe the target is in a different location.

**Source:** `= this.source` (`= this.source-type`)
