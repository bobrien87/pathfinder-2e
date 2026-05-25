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

**Effect** You sway in a loose stance that lets you sweep in wide arcs with the claws on your feet. The only Strikes you can make are spinning talon unarmed attacks. These deal 1d8 slashing damage, are in the brawling group, and have the finesse, sweep, and unarmed traits. You don't need a free hand to use spinning talon strikes.

**Source:** `= this.source` (`= this.source-type`)
