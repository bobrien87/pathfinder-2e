---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Samsaran|Samsaran]]"
traits: ["[[Samsaran]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your past lives have provided heightened insight to the spiritual world and current and future events, as history repeats itself. Choose arcane, divine, or occult. You gain one cantrip from that magical tradition's spell list. You can Cast this Spell as an innate spell at will, as a spell of your chosen tradition. A cantrip is heightened to a spell rank equal to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
