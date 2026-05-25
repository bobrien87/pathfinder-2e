---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Attack]]", "[[Composite]]", "[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Spinning molten iron through a vortex of fire, you trap your foe in searing wires. Make an Impulse check{impulse attack} roll against a creature within 15 feet. On a success, the target takes @Damage[(floor((@actor.level -6)/4)+2)d6[slashing]] damage and is wrapped in molten wire for 1 minute. It is [[Clumsy]] 1 and takes @Damage[(floor((@actor.level -6)/4)+2)d4[fire]] damage at the start of each of its turns, with a basic Reflex save. The wire's [[Escape]] DC is your class DC. The wire has AC 10 and 75 HP. The impulse ends if the creature Escapes or the wire is destroyed.

**Level (+4)** The slashing damage increases by 1d6, the fire damage increases by 1d4, and the wire's HP increases by 25.

**Source:** `= this.source` (`= this.source-type`)
