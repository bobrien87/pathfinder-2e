---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Metal]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Ragged pieces of metal weld together into a ramshackle structure. The barricade is up to 30 feet long, 15 feet high, and 1/2 inch thick. It must form in a straight line within 120 feet in an unbroken open space that doesn't pass through any creatures or objects, or the impulse fails. Each 10-foot-by-10-foot section of the wall has AC 10, Hardness 10, and 20 Hit Points, and it's immune to critical hits and precision damage. If any section is destroyed, the entire wall collapses, and each creature adjacent to the wall takes @Damage[(floor((@actor.level -6)/2)+2)d8[slashing]] damage with a [[Reflex]] save against your class DC. The wall lasts until the end of your next turn, but you can Sustain it up to 1 minute.

**Level (+2)** The maximum length of the wall increases by 10 feet, the HP of each section increases by 10, and the damage when it's destroyed increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
