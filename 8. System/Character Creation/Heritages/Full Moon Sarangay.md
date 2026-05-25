---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Sarangay|Sarangay]]"
traits: ["[[Sarangay]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were raised in a shamanic tradition transcending a single sarangay community or heritage. You spent your youth under the guidance of a shaman elder, who taught you to commune with spirits in the hope that you'll one day use that knowledge to advise and guide your people. Those from your tradition are priests or shamans who channel the spirits and see things others can't. You gain an ancestry attribute boost to Wisdom instead of Strength, and you gain an attribute flaw in Constitution instead of Wisdom. You gain the [[Folk Healer]] ancestry feat.

**Source:** `= this.source` (`= this.source-type`)
