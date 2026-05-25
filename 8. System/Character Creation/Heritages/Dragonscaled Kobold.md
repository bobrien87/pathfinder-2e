---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kobold|Kobold]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Thanks to your warren's association with a dragon, your scales are sturdier than other kobolds'. You gain 10 Hit Points from your ancestry instead of 6. You gain a +1 circumstance bonus to saves against dragon breath, effects with the sleep trait, and effects that would make you [[Paralyzed]].

**Source:** `= this.source` (`= this.source-type`)
