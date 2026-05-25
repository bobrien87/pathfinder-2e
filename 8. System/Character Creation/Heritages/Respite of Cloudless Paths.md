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

You swore a vow to protect the waylaid and the lost. Both environmental heat effects and environmental cold effects are one step less extreme for you (incredible heat becomes extreme, extreme cold becomes severe, and so on), and you gain a + 1 circumstance bonus to saving throws against environmental features or hazards, such as floods, rockslides, and sandstorms.

**Additional Edict** assist lost or incapacitated travelers

**Source:** `= this.source` (`= this.source-type`)
