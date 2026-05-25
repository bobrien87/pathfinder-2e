---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Automaton|Automaton]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Sporting a bulkier, powerful design, your body has been designed for combat. You have a bulky, humanoid shape. The damage die for your fist increases to 1d6 instead of 1d4. You don't take a penalty when making a lethal attack with your fist or any other unarmed attack.

**Source:** `= this.source` (`= this.source-type`)
