---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Elf|Elf]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have an inborn ability to detect and understand magical phenomena. You can cast the [[Detect Magic]] cantrip as an arcane innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up.

In addition, you gain a +1 circumstance bonus to checks to [[Identify Magic]] and to [[Decipher Writing]] of a magical nature. These skill actions typically use the Arcana, Nature, Occultism, or Religion skill.

**Source:** `= this.source` (`= this.source-type`)
