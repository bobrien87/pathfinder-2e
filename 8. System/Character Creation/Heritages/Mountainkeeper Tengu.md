---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Tengu|Tengu]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You come from a line of tengu ascetics, leaving you with a link to the spirits of the world and the Great Beyond. You can cast the [[Vitality Lash]] cantrip as a primal innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up. Each time you cast a spell from a tengu heritage or ancestry feat, you can decide whether it's a divine or primal spell.

**Source:** `= this.source` (`= this.source-type`)
