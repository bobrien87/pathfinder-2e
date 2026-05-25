---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** You force a temporary pact on both yourself and another creature you can see within 60 feet. Choose attack, move, manipulate, or concentrate. The target must attempt a Will saving throw.
- **Success** The target is unaffected.
- **Failure** If you or the target uses an action with the chosen trait within the next minute, they take 10d6 mental damage, and this pact ends for both of you.
- **Critical Failure** As failure, except your target takes the damage if either of you uses an action with the chosen trait.

**Source:** `= this.source` (`= this.source-type`)
