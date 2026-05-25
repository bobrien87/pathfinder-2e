---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Eidolon]]"]
cast: "`pf2:0`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per minute

**Requirements** Your eidolon is dispersed.

Your eidolon focuses on inflicting the most damage possible on its foes. If your eidolon's next action is to use [[Swarming Assault]], the number of damage dice of the Swarming Assault are doubled. Additionally, creatures that fail their Reflex save against that Swarming Assault are [[Sickened]] 2 ([[Sickened]] 4 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
