---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Investigator]]"]
cast: "`pf2:r`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

**Trigger** Another creature attempts a check that could help get you closer to answering the question at the heart of one of your active investigations.

You share information with the triggering creature. They gain a circumstance bonus to their check equal to your investigation bonus from Pursue a Lead. The GM can add any relevant traits to this reaction depending on the situation, such as auditory and linguistic if you're conveying information verbally.

> [!danger] Effect: Clue In

**Source:** `= this.source` (`= this.source-type`)
