---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kobold|Kobold]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Since hatching in the vicinity of a powerful source of magic, a trace of it flows through your veins. Choose one common cantrip from the arcane spell list. You can Cast this Spell as an arcane innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up. You are trained in the spell attack modifier and spell DC statistics, and your key spellcasting attribute is Charisma.

**Source:** `= this.source` (`= this.source-type`)
