---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Samsaran|Samsaran]]"
traits: ["[[Samsaran]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your past incarnations were reborn in sanctuaries in northern Zi Ha, and you have recollections of being trained to concentrate and focus for long periods of time. Your hazy flashbacks also reveal useful scripture in the books your past lives had eagerly consumed. You gain the [[Tap the Past]] action.

**Source:** `= this.source` (`= this.source-type`)
