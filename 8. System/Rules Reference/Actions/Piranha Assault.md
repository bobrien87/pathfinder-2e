---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

You know that a thousand small bites can fell a large foe just as surely a single well-placed hit. Designate a creature within the aura of your commander's banner and signal all squadmates; for 1 minute, each time they attack that creature and deal damage to it of a type the creature resists, they ignore an amount of that creature's resistance equal to your level.

**Source:** `= this.source` (`= this.source-type`)
