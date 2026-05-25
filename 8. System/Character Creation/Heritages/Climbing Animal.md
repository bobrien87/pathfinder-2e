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

You are an animal whose limbs are adapted to grab, climb, and brachiate. You might be dexterous and ready to use tools like a chimpanzee or otter, or you may simply be a quick climber like a bear, raccoon, or sloth.

You have a land Speed of 20 feet, a climb Speed of 20 feet, and one animal attack of your choice (typically claw, fist, or jaws).

**Source:** `= this.source` (`= this.source-type`)
