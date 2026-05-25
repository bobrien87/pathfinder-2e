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

The chamber housing your core has a more direct connection to the rest of your humanoid shape, allowing you to tap into your core's magical energy. You gain one cantrip from the arcane spell list. You can cast this spell as an arcane innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
