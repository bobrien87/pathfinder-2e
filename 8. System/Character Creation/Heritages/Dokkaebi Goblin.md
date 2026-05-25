---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Goblin|Goblin]]"
traits: ["[[Goblin]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your ancestors mastered illusion-based magic, giving you an innate understanding of it. You can cast [[Figment]] as an innate occult cantrip at will. A cantrip is heightened to a spell rank equal to half your level rounded up. You also gain a +1 circumstance bonus to Will saves against illusions.

**Source:** `= this.source` (`= this.source-type`)
