---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Eidolon]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your eidolon is condensed.

Your eidolon suddenly shifts itself into a terrifying shape of its choosing, rather than a simple mound, by closely controlling the positioning of its component bodies. The eidolon attempts to `act demoralize` a creature within 15 feet; this Demoralize attempt loses the auditory trait, gains the visual trait, and the eidolon doesn't take a –4 circumstance penalty to the check if they don't share a language with their target. On a success or critical success, the target is additionally [[Off Guard]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
