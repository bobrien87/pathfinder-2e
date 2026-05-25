---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Cold]]", "[[Impulse]]", "[[Incapacitation]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Intense cold swirls around your foe, covering it in frost that slows it down and turns its body to ice. Target a creature you can observe within 120 feet. It must attempt a [[Fortitude]] save against your class DC. The creature is then temporarily immune for 24 hours.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Slowed]] 1 until the end of its next turn.
- **Failure** The target is frozen solid. It can't act, its AC is 9, it has Hardness 5, and it's immune to other cold effects, critical hits, and precision damage. This lasts until the end of your next turn, but if the target is affected by a hostile action, this effect ends immediately after that action.
- **Critical Failure** As failure, but after becoming unfrozen, the creature is slowed 1 until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
