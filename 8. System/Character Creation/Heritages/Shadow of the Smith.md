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

Your shadow is thick and liquid, like it could quench the finest ore. You gain the [[Inscribe Shadow Pamor]] action.

**Source:** `= this.source` (`= this.source-type`)
