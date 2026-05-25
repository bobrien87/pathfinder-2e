---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Awakened Animal|Awakened Animal]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You are an animal meant for running at great speeds across land. Typically, you run on all fours like a dog, cheetah, or an iguana, but you could also use two legs like a kangaroo, emu, or penguin.

You have a land Speed of 30 feet and one animal attack of your choice (typically claw, jaws, or tail).

**Source:** `= this.source` (`= this.source-type`)
