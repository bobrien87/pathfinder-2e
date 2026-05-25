---
type: action
source-type: "Remaster"
traits: ["[[Earth]]", "[[Transcendence]]", "[[Visual]]"]
cast: "`pf2:1`"
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You Raise your [[Mirrored Aegis]], though it seems to lose some of its usual luster in favor of the dull sheen of stone. If you [[Shield Block]] a melee attack with the mirrored aegis before the beginning of your next turn, the gorgon's eyes upon it flash at the triggering creature, who must attempt a [[Fortitude]] save against your class DC. On a failure, they are [[Slowed]] 1 for 1 minute as their body partially petrifies. Regardless of the outcome, that creature is temporarily immune to this effect for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
