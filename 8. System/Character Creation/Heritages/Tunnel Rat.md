---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Ratfolk|Ratfolk]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You can easily compress your body and squeeze through gaps. You gain the [[Quick Squeeze]] feat as a bonus feat, even if you aren't trained in Acrobatics. Tight spaces not tight enough to require the [[Squeeze]] action aren't difficult terrain for you.

**Source:** `= this.source` (`= this.source-type`)
