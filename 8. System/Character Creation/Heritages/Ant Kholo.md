---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kholo|Kholo]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You're a sharp-featured, big-eared kholo about 3 feet tall. Many are skeptical that you are in fact a kholo. Your size is Small instead of Medium. You are trained in Deception (or another skill if you were already trained in Deception). You gain a +1 circumstance bonus to Deception checks to Lie when specifically claiming innocence, to Deception DCs against [[Sense Motive]] checks to uncover such lies, and to initiative checks when you roll Deception for initiative.

**Source:** `= this.source` (`= this.source-type`)
