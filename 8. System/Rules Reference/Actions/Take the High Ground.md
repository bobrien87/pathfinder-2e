---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your ally leaps to secure the high ground with a little help from the squad. Signal a squadmate within the aura of your commander's banner; as a free action, that squadmate can Stride directly toward any other squadmate you are both observing. If the first squadmate ends this movement adjacent to another squadmate, the first squadmate can immediately [[Leap]] up to 25 feet horizontally or 15 feet vertically as a reaction, boosted by the other squadmate. This distance increases to 40 feet horizontally or 25 feet vertically if you have legendary proficiency in Warfare Lore.

**Source:** `= this.source` (`= this.source-type`)
