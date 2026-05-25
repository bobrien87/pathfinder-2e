---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Sprite|Sprite]]"
traits: ["[[Sprite]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have the head of a goldfish or carp and scales that come in an auspicious combination of stark white, black, orange, red, and gold. If you gain wings, they appear much like the wispy hairs of a dragon. You gain a swim Speed of 10 feet and the amphibious trait. Like all creatures with the amphibious trait, you can breathe both water and air.

**Source:** `= this.source` (`= this.source-type`)
