---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Jotunborn|Jotunborn]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were chosen for your smaller size that allows you to move between planar thresholds with ease. You generally serve as a messenger or scout, and planar exposure has granted you a spark of magical power. Instead of Large, your size is Medium. You gain one cantrip from the occult spell list. You can cast this spell as an occult innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
