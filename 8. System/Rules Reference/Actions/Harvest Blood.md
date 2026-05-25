---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your last action was a successful piercing or slashing melee Strike against a creature that is not immune to bleed

**Effect** You consume the blood lingering upon your weapon. You reduce the value of your drained condition by 1, gain temporary Hit Points equal to your Constitution modifier, and gain a +1 circumstance bonus to saving throws against that creature's spells for 1 minute, or until you Harvest Blood from another creature.

**Source:** `= this.source` (`= this.source-type`)
