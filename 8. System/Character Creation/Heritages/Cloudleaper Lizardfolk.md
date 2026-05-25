---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Lizardfolk|Lizardfolk]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your body is light with flaps of skin along your limbs that catch the air that passes beneath you. As long as you can act and have enough room, you can open the flaps to slow any fall just enough to avoid taking damage (whether you have the room to do so depends on the GM's discretion).

**Source:** `= this.source` (`= this.source-type`)
