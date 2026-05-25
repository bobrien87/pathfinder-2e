---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Linguistic]]", "[[Mental]]", "[[Mythic]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** You proclaim an ultimatum against a creature you believe is oppressing others and all who follow their orders. All other creatures (including you) who hear your ultimatum, or learn about it later on, are emboldened by your words for 1 day, and gain a +2 status bonus to their Will saving throws against effects produced by the oppressing creature and their allies, which increases to +3 if they are within 30 feet of you.

> [!danger] Effect: Ultimatum of Liberation

Additionally, the first time each day that creature and each of its allies comes within 30 feet of you, they must succeed on a [[Will]] save against your class DC or spell DC (whichever is higher) or become [[Frightened]] 1 ([[Frightened]] 2 on a critical failure). This second effect has the emotion, fear, and mental traits. The oppressing creature may end all the effects as a free action by truthfully agreeing to permanently end their oppression. Otherwise, your Ultimatum of Liberation has no duration, though you can have only one Ultimatum of Liberation active at a time. If you pronounce a second Ultimatum of Liberation, the effects of the first one end.

**Source:** `= this.source` (`= this.source-type`)
