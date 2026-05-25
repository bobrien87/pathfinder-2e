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

You are native to arid plains and likely grew up traveling the roads. If you have both hands free, you can increase your Speed to 30 feet as you run on all fours. In addition, environmental heat effects are one step less extreme for you, and you can go 10 times longer than normal before you are affected by starvation or thirst. However, unless you wear protective gear or take shelter, environmental cold effects are one step more extreme for you.

**Source:** `= this.source` (`= this.source-type`)
