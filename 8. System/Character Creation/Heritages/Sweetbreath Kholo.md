---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kholo|Kholo]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You're a striped, pale-furred kholo with oddly pleasant breath, which you can use to entrance your prey. You are trained in Diplomacy (or another skill if you were already trained in Diplomacy). You also gain a +1 circumstance bonus to checks to [[Make an Impression]] if the target can smell your breath.

**Source:** `= this.source` (`= this.source-type`)
