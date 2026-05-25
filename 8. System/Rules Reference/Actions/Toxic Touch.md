---
type: action
source-type: "Remaster"
traits: ["[[Poison]]"]
cast: "`pf2:1`"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Requirements** Your most recent action was to [[Tumble Through]], and you successfully moved through an enemy's space

**Effect** Make a melee unarmed Strike against the enemy whose space you moved through. On a hit, the target takes 1d6 persistent,poison damage and is [[Sickened]] 1 (or takes 2d6 persistent,poison and is [[Sickened]] 2 on a critical hit).

**Source:** `= this.source` (`= this.source-type`)
