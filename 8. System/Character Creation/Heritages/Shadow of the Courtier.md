---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Wayang|Wayang]]"
traits: ["[[Wayang]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your shadow dances alongside you. You gain the Impressive Performance skill feat, allowing you to [[Make an Impression]] using Performance instead of Diplomacy. Once per day, if you fail, but not critically fail, a check to Make an Impression, you can play it off as part of a performance, allowing you to reroll the check; this is a fortune effect.

**Source:** `= this.source` (`= this.source-type`)
