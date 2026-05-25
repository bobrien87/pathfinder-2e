---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Leshy|Leshy]]"
traits: ["[[Leshy]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your leshy spirit took hold in a massive peach fruit before your body split forth from it, possibly emulating a past hero who was born in the same manner. You look like a human child, though with a perpetual flush of pink to your complexion and perhaps a few peach leaves growing from your body. The nature spirit inside you puts certain animals at ease.

You can ask questions of and receive answers from household animals and livestock, such as dogs or pheasants, as well as use Diplomacy to Make an Impression on and Request things of them. Most domesticated animals have an indifferent or friendly starting attitude toward you and give you time to make your case, though other animals react to you like any other adventurer.

**Source:** `= this.source` (`= this.source-type`)
