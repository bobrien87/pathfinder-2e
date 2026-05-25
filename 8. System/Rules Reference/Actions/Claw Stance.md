---
type: action
source-type: "Remaster"
traits: ["[[Stance]]"]
cast: "`pf2:1`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Effect** You extend the claws in your hands and focus your attention to take down single targets. The only Strikes you can make are frenzied claw unarmed attacks. These deal 1d6 slashing damage, are in the brawling group, and have the agile, finesse, grapple, unarmed, and versatile piercing traits.

**Source:** `= this.source` (`= this.source-type`)
