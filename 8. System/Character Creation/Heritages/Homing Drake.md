---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Dragonet|Dragonet]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have a short, stubby nose, and tiny spines that resemble hairs. You might have vividly colored scales or be a dun brown. You can cast the [[Know the Way]] cantrip as an arcane innate spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up.

In addition, you always know the distance and direction to your home. You can designate a new location as your home after you spend 1 week there, but you can have only a single designated home at a time.

**Source:** `= this.source` (`= this.source-type`)
