---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per round

**Effect** You Interact to reload a sling or blowgun and then Strike. If the Strike is successful and you were undetected or unnoticed by the target when you made the attack, you are now [[Hidden]] from the target after the attack, as they cannot tell where the attack came from.

**Source:** `= this.source` (`= this.source-type`)
