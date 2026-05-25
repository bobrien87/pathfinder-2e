---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Composite]]", "[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Stance]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You shape your kinetic aura into swirling armor of steam that scalds your enemies and propels you on super-heated jet streams. A creature can take damage from Steam Knight only once per round. Your steam armor has the following effects.

- You gain a +10-foot status bonus to your Speed.

- When you [[Leap]], you can jump up to your Speed. You don't immediately fall at the end of a jump, provided you Leap again with your next action. If you Leap over a creature and come within 10 feet, that creature takes @Damage[(floor((@actor.level -6)/5)+2)d6[fire]] damage with a [[Reflex]] save against your class DC.

- At the start of each of your turns, you can emit steam as a free action. It deals @Damage[(floor((@actor.level -6)/5)+2)d6[fire]] damage to each creature in your kinetic aura with a [[Reflex]] save against your class DC. A creature that fails is also pushed 5 feet.

**Level (+5)** The fire damage from a jump or blast of steam increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
