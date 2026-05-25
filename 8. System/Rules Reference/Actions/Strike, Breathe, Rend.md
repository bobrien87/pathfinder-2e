---
type: action
source-type: "Remaster"
traits: ["[[Spirit]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your last action this turn was a successful Strike with the [[Noble Branch]]

**Effect** You channel a rending pulse of energy down your weapon in the moment of contact. The target of the Strike takes spirit damage equal to the noble branch's weapon damage dice. This includes any extra dice from striking runes, but not from special abilities, property runes, or the like.

**Source:** `= this.source` (`= this.source-type`)
