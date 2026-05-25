---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Fortune]]"]
cast: "`pf2:0`"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You attempt a skill check directly related to the conditions of the pact

**Frequency** once per hour

**Effect** You call upon the occult energies powering your pact to help you fulfill your promise. Roll twice on the triggering check and take the better result.

**Source:** `= this.source` (`= this.source-type`)
