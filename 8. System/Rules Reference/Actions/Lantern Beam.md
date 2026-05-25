---
type: action
source-type: "Remaster"
traits: ["[[Fire]]", "[[Light]]", "[[Magical]]"]
cast: "`pf2:1`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your lantern light is shining

**Effect** Your lenses focus your light into a searing beam. You deal @Damage[((max(5,ceil(@actor.level/2)))d4)[fire]|options:area-damage] damage to all creatures in a @Template[line|distance:30], with a [[Reflex]] save saving throw against the higher of your class DC or spell DC. Your lantern light then extinguishes, and you can't use this ability or use your lantern light again for 1d4 rounds. At 11th level and every two levels thereafter, the damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
