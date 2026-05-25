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

Your toes are adapted for gripping and climbing. You gain the [[Combat Climber]] feat as a bonus feat, and as long as you aren't wearing footwear, you can use the sticky pads on your feet to climb, leaving your hands free. Additionally, if you roll a success on an Athletics check to climb, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
