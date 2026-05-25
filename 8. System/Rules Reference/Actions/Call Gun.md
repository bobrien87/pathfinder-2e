---
type: action
source-type: "Remaster"
traits: ["[[Magical]]"]
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Effect** You hold aloft a free hand and call the firearm or crossbow you chose during your daily preparations into your hand. As long as the weapon you chose is on the same plane, it appears in your hand.

**Source:** `= this.source` (`= this.source-type`)
