---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Lizardfolk|Lizardfolk]]"
traits: ["[[Lizardfolk]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have a trunk-like snout and a connection to the divine. The tradition of any spells or magical abilities you gain from a lizardfolk heritage or ancestry feat is divine instead of its normal tradition (usually primal).

You gain your choice of the [[Divine Lance]] or [[Forbidding Ward]] cantrips, which you can cast as a divine innate cantrip at will. A cantrip is heightened to a spell rank equal to half your level rounded up. When you cast this cantrip, it loses the manipulate trait, as you cast purely by roaring and flaring your trunk.

**Source:** `= this.source` (`= this.source-type`)
