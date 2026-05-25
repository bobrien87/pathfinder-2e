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

You swore a vow to release others from natural calamities. Your vow grants you the strength to carry 1 more Bulk than normal before becoming encumbered and up to a maximum of 2 more Bulk, as well as a +1 circumstance bonus to Athletics checks to [[Force Open]] or [[Escape]].

**Additional Edict** do your utmost to aid or rescue those trapped or affected by natural disasters

**Source:** `= this.source` (`= this.source-type`)
