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

You move easily through thick forest and jungle, using every branch or bush. You can always use the [[Take Cover]] action when in forest or jungle terrain to gain cover, even if you're not next to an obstacle you would normally be able to Take Cover behind. You gain the [[Terrain Stalker]] feat, even if you're not trained in Stealth, and you must choose underbrush as your chosen terrain.

**Source:** `= this.source` (`= this.source-type`)
