---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Air]]", "[[Electricity]]", "[[Impulse]]", "[[Kineticist]]", "[[Move]]", "[[Overflow]]", "[[Polymorph]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

For an instant, you transform yourself into a being of pure lightning and fly forward, shocking anyone in your way. You propel yourself forward in a @Template[line|distance:30]. You can move through creatures during this movement, and this movement doesn't trigger reactions that are triggered by movement. Each creature you move through takes @Damage[(floor((@actor.level -4)/3)+2)d12[electricity]|options:area-damage] damage with a [[Reflex]] save against your class DC. You return to your normal form in the final square of the line. If you're in the air, you fall unless you have a fly Speed.

**Level (+3)** The length of the line increases by 5 feet, and the damage increases by 1d12.

**Source:** `= this.source` (`= this.source-type`)
