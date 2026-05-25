---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Air]]", "[[Illusion]]", "[[Impulse]]", "[[Kineticist]]", "[[Mental]]", "[[Overflow]]", "[[Primal]]", "[[Visual]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

An illusion of a limitless expanse with an impossibly blue sky makes all within feel the sensation of falling... forever. The vision appears in a @Template[burst|distance:20] within 100 feet. The illusion lasts until the end of your next turn, but you can Sustain it up to 1 minute. Using this impulse again ends any previous one. Each creature in the area or that later enters it must attempt a [[Will]] save against your class DC. Creatures with the air trait are immune. Any effect of the illusion ends for a creature as soon as it leaves the illusion's area or the impulse ends, and the creature then becomes temporarily immune for 1 hour.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Off Guard]].
- **Failure** The creature is off-guard. It is [[Fleeing]] from the illusory sky but is also disoriented; any time it uses an action to attempt to flee, it must succeed at a DC 11 flat check or flee to a space that's still within the illusion. The GM determines where the creatures ends up, but the creature can't stay stationary if it's able to move.

**Source:** `= this.source` (`= this.source-type`)
