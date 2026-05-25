---
type: action
source-type: "Remaster"
traits: ["[[Divine]]", "[[Earth]]"]
cast: "`pf2:2`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** Thick slabs of stone rise around you before tilting over. You deal @Damage[(ceil(@actor.level/2)d6)[bludgeoning]] damage to all adjacent creatures ([[Reflex]] save against your class DC or spell DC, whichever is higher). On a critical failure, the creature is also knocked [[Prone]]. At 3rd level, and every 2 levels thereafter, this damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
