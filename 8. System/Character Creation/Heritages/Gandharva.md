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

You're descended from the self-proclaimed musicians, poets, and dancers of the gods, with a body that's part humanoid and part horse or bird. If you gain wings, they come in many different brilliant colors. Due to your celestial connection, the tradition of any spells or magical abilities you gain from a sprite heritage or ancestry feat is divine instead of its normal tradition.

You become trained in Performance (or another skill of your choice if you're already trained in Performance), and you can cast [[Summon Instrument]] as a divine innate cantrip.

**Source:** `= this.source` (`= this.source-type`)
