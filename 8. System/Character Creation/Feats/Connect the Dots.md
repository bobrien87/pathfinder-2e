---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Investigator]]", "[[Linguistic]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Ephemeral connections between people, places, and concepts are invisible to most, but seeing them is your stock and trade. Choose an ally and a non-allied creature. You must be able to see both of them. You briefly study the way they both move and attempt a [[Perception]] check against the higher of the non-allied creature's Deception DC or Will DC. Both targets are then temporarily immune to Connect the Dots for 10 minutes.
- **Critical Success** You spot a way for your ally to take advantage of the other target's flaws and let them know about it. Your ally gains your [[Pursue a Lead]] investigation bonus as a circumstance bonus to all its Strikes or skill checks against the creature until the start of your next turn.
- **Success** As critical success, but your ally gains the bonus only for their next Strike or skill check against the creature.

> [!danger] Effect: Connect the Dots
- **Failure** You fail to make a connection.
- **Critical Failure** You misconstrue a vital piece of information, which temporarily disconcerts you. You are [[Stupefied 1]] until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
