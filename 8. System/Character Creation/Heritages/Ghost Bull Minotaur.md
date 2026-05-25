---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Minotaur|Minotaur]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your fur is as pale as death, possibly from some connection you or your family has to the afterlife, which lets you supernaturally find your way. You can cast [[Know the Way]] as an occult innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up. In addition, you gain a +1 circumstance bonus against spells or effects that cause the [[Confused]] condition.

**Source:** `= this.source` (`= this.source-type`)
