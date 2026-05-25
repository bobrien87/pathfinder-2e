---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Merfolk|Merfolk]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

The lower half of your body resembles a powerful sailfish, complete with a large dorsal fin. Using this fin, you can move through the water faster and leap farther. Your swim Speed increases to 30 feet. When you attempt a [[High Jump]] or [[Long Jump]], you gain a +1 circumstance bonus to the Athletics check, and you can Swim instead of Striding before attempting the jump.

**Source:** `= this.source` (`= this.source-type`)
