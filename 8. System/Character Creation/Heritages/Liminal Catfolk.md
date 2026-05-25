---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Catfolk|Catfolk]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You've inherited a closeness to the far corners of the world, where the boundaries between dimensions grow thin. You can cast the [[Detect Magic]] cantrip as an occult innate spell at will. A cantrip is heightened to half your level rounded up. You also gain a +1 circumstance bonus to Occultism checks to [[Recall Knowledge]] about creatures that originated on planes other than the Universe.

**Source:** `= this.source` (`= this.source-type`)
