---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kobold|Kobold]]"
traits: ["[[Kobold]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your proximity to a mighty kaiju has caused you to grow strong and hardy. You gain 10 Hit Points from your ancestry instead of 6. Instead of the normal attribute boosts and flaws, you can choose to gain a boost to Strength, a boost to Charisma, and a flaw in Intelligence.

**Source:** `= this.source` (`= this.source-type`)
