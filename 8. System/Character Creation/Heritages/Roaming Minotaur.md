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

Your hooves are broad and powerful, perfect for clearing away rubble as you step. You become trained in Survival (or another skill if you were already trained in Survival) and gain the [[Terrain Expertise]] skill feat. You ignore difficult terrain caused by natural uneven ground while in the terrain chosen for your Terrain Expertise feat.

**Source:** `= this.source` (`= this.source-type`)
