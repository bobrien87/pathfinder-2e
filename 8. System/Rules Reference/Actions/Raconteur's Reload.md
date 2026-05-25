---
type: action
source-type: "Remaster"
traits: ["[[Gunslinger]]"]
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your rapid or forceful words draw the enemy's attention away from your hands long enough to chamber another bullet. Interact to reload and then attempt a Deception check to Create a Diversion or an Intimidation check to `act demoralize`.

**Source:** `= this.source` (`= this.source-type`)
