---
type: action
source-type: "Remaster"
traits: ["[[Magical]]", "[[Spellshot]]", "[[Teleportation]]"]
cast: "`pf2:r`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You miss with a firearm or crossbow Strike.

You create a bond to your ammunition, calling your missed shot back. The ammunition you just fired is reloaded back into your weapon. If the ammunition was a piece of magical or alchemical ammunition that normally requires one or more actions to activate, you must re-activate it before firing again.

**Source:** `= this.source` (`= this.source-type`)
