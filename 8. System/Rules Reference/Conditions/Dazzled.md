---
type: condition
source-type: "Remaster"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

Your eyes are overstimulated or your vision is swimming. If vision is your only precise sense, all creatures and objects are [[Concealed]] from you.

**Source:** `= this.source` (`= this.source-type`)
