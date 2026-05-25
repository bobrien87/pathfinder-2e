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

You have the head of a mouse deer and hooves instead of feet, with a reputation for being clever and persuasive—able to get yourself out of sticky situations with wordplay and a bit of luck. You become trained in Deception (or another skill if you were already trained in Deception). You gain a +1 circumstance bonus to Deception checks to Lie when specifically attempting to avoid danger or punishment (such as trying to convince a dragon not to eat you), to Deception DCs against [[Sense Motive]] checks to uncover such lies, and to initiative rolls when you roll Deception for initiative.

**Source:** `= this.source` (`= this.source-type`)
