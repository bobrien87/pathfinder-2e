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

You were born with big, expressive ears that move with your moods and perk up at any unexpected sound. You gain a +2 circumstance bonus to locate undetected creatures that you could hear within 30 feet with a [[Seek]] action. As long as you're aware of a creature via sound, once per round, your ears can help you [[Point Out]] the creature to all allies as a free action.

**Source:** `= this.source` (`= this.source-type`)
