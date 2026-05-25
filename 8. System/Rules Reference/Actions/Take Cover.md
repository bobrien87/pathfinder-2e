---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are benefiting from standard cover, are near a feature that allows you to take cover, or are [[Prone]].

You press yourself against a wall or duck behind an obstacle to take better advantage of cover. If you would have standard cover, you instead gain greater cover, which provides a +4 circumstance bonus to AC; to Reflex saves against area effects; and to Stealth checks to `act hide`, `act sneak`, or otherwise avoid detection. Otherwise, you gain standard cover (a +2 circumstance bonus instead). If you're prone, you gain greater cover against ranged attacks. Take Cover lasts until you move from your current space, use an attack action, become [[Unconscious]], or end it as a free action.

**Source:** `= this.source` (`= this.source-type`)
