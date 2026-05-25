---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kholo|Kholo]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You're a shaggy, dark-furred kholo capable of making some truly uncanny sounds. You can cast the [[Figment]] cantrip as an occult innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up. In addition, you gain a +1 circumstance bonus to checks to [[Create a Diversion]] and Impersonate when using only your voice.

**Source:** `= this.source` (`= this.source-type`)
