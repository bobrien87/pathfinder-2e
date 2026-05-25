---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Exploration]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

If you're an arcane spellcaster who prepares from a spellbook, you can attempt to prepare a spell from someone else's spellbook. The GM sets the DC for the check based on the spell's rank and rarity; it's typically a bit easier than [[Learning the Spell]].
- **Success** You prepare the borrowed spell as part of your normal spell preparation.
- **Failure** You fail to prepare the spell, but the spell slot remains available for you to prepare a different spell. You can't try to prepare this spell until the next time you prepare spells.

**Source:** `= this.source` (`= this.source-type`)
