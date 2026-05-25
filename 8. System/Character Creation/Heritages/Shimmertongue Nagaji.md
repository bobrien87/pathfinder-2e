---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Nagaji|Nagaji]]"
traits: ["[[Nagaji]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were born with a keen sense for magic, able to taste its unique effects in the air. You gain magicsense as a vague sense that has a range of 30 feet—like all vague senses, it's only about as precise as an average human's sense of smell, meaning you generally can predict only if magic is present; however, each tradition of magic has a unique taste to you, allowing you to identify the tradition of magic present.

**Source:** `= this.source` (`= this.source-type`)
