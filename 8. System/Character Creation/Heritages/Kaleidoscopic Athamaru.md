---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Athamaru|Athamaru]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your scales are a spectrum of color that shimmers in the light. In areas of bright light or dim light, you gain a +1 circumstance bonus to Performance checks. You also gain the [[Dazzle Seeker]] reaction.

**Source:** `= this.source` (`= this.source-type`)
