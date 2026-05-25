---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Yaksha|Yaksha]]"
traits: ["[[Yaksha]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You swore a vow to shelter and feed the poor. Your vow grants you adroitness with carpentry, cook pot, and cloth; you become trained in Crafting and Cooking Lore, and you gain the [[Improvise Tool]] skill feat.

**Additional Edict** help the impoverished to the extent you're able by repairing their abodes and clothing or by feeding them

**Source:** `= this.source` (`= this.source-type`)
