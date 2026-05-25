---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Yaoguai|Yaoguai]]"
traits: ["[[Yaoguai]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were a simple animal until the sun enlightened you.

- **Humanoid Form** Animals can sense the power of your presence. You gain a +1 circumstance bonus to Intimidation checks against animals and beasts and don't take a penalty for attempting to Intimidate animals or beasts you don't share a language with.
- **Yaoguai Form** You can dash like an animal. If you have both hands free, you can increase your Speed to 30 feet as you run on all fours.

**Source:** `= this.source` (`= this.source-type`)
