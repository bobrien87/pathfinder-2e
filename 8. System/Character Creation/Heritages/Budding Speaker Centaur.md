---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Centaur|Centaur]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were born with a spark of magic that could set you on the path to becoming a Greenspeaker or Faithspeaker. Select divine or primal. If you selected divine, you're a Faithspeaker. If you selected primal, you're a Greenspeaker. This choice can't be changed. You gain one cantrip from the chosen spell list. You can cast this spell as an innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
