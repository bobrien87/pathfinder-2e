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

You look like a human child, though with a grand crown of chrysanthemums growing from your head, ornate as an emperor's. These petals have medicinal properties, granting you a +1 circumstance bonus to saving throws against poison.

Furthermore, during your daily preparations, you can harmlessly pluck a few petals from your head and steep them in fresh water to create a single Lesser Antidote, which takes the form of a tea. At level 6, you instead create a Moderate Antidote; at level 10, a Greater Antidote; and at level 14, a Major Antidote. The tea loses its effectiveness if not consumed before your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
