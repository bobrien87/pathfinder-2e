---
type: action
source-type: "Remaster"
traits: ["[[Mythic]]"]
cast: "`pf2:r`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your turn begins

**Effect** You make a Strike against one opponent within your reach, or Stride directly towards an opponent. If this is the first time you've struck that opponent during this encounter, the Strike is made at mythic proficiency.

**Source:** `= this.source` (`= this.source-type`)
