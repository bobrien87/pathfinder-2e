---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Minotaur|Minotaur]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Despite your heavy frame, you walk on shaggy hooves that muffle your footfalls, allowing you to surprise your prey. You become trained in Stealth (or another skill if you were already trained in Stealth) and gain the [[Terrain Stalker]] skill feat, except you must choose rubble and you can [[Sneak]] no more than 10 feet instead of 5 feet without attempting a Stealth check.

**Source:** `= this.source` (`= this.source-type`)
