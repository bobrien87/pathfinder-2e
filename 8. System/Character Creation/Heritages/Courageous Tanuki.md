---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Tanuki|Tanuki]]"
traits: ["[[Tanuki]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your heart beats with the courage of those who came before you, giving you the kind of bravery only a tanuki can demonstrate. Whenever you gain the [[Fleeing]] condition, you also gain a +10-foot circumstance bonus to your Speeds that lasts as long as you're fleeing. When you have the fleeing condition, instead of having to spend all your actions trying to escape, you can act normally for one action but must still spend the remainder of your actions fleeing. You also gain the [[Tactical Retreat]] ability.

**Source:** `= this.source` (`= this.source-type`)
