---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Gnome|Gnome]]"
traits: ["[[Gnome]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your ancestors lived in the trees and fished in all the waters of Tian Xia. You gain your choice of the following benefits. Once made, this choice can't be changed.

- You can climb any banyan. You gain the [[Combat Climber]] feat, and if you roll a success on the Athletics check to Climb, you get a critical success instead.
- You can catch any fish. You gain a swim Speed of 15 feet.

**Source:** `= this.source` (`= this.source-type`)
