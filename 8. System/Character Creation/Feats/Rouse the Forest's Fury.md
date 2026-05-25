---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Plant]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Terrifying trees attack your enemies. Three Large trees appear in unoccupied spaces within 500 feet, at least 15 feet from one another. Each tree has AC 40, Fortitude +33, Reflex +24, Will +30, and 200 HP. The trees can flank, but are unable to move. When the trees appear, each makes a Strike; they share a multiple attack penalty. The tree's melee Strike is a branch that has reach 10 feet; on a hit, the target is [[Grabbed]] by the tree (+30 attack modifier and deals @Damage[(ternary(gte(@actor.level, 20), 5, 4)d10+9)[bludgeoning]] damage.

The trees last until the end of your next turn, and you can Sustain the impulse. Each time you Sustain the impulse, you can have one tree make a Strike.

**Level (20th)** The attack modifier is +32 and the Strike damage is 5d10+9.

**Source:** `= this.source` (`= this.source-type`)
