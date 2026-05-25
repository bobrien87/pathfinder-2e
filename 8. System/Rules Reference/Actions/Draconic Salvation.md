---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Fortune]]"]
cast: "`pf2:r`"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You critically fail a saving throw against an effect with the same tradition trait as your draconic benefactor (for instance, a divine spell if your benefactor is a diabolic dragon)

**Requirements** Your spectral dragon is in your space

**Effect** You improve your saving throw result by one degree of success, and Channel Draconic Essence ends.

**Source:** `= this.source` (`= this.source-type`)
