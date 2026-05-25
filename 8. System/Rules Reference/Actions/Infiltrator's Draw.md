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

**Effect** You Interact to draw a gauntlet bow, hand crossbow, or repeating hand crossbow, then Strike with it. Alternatively, you can Strike with a loaded hand crossbow or repeating hand crossbow you're already holding and then Interact to stow it.

**Source:** `= this.source` (`= this.source-type`)
