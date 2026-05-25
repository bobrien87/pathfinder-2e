---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Plant]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You conjure a massive willow tree, which lashes your foes with a thousand branches. The trunk of the weeping willow tree is 10-feet in diameter and appears in an unoccupied space within 500 feet. The tree whips its branches at all your enemies within a @Template[emanation|distance:30]{30-foot-radius emanation} centered on the willow's trunk, dealing @Damage[(10 + floor(@actor.level/20)*4)d8[slashing]|options:area-damage] damage with a [[Reflex]] save against your class DC. A creature that fails its save is also overcome with sorrow, becoming [[Slowed]] 1 for as long as the willow remains, as it weeps uncontrollably. The willow doesn't target you or your allies.

The willow tree remains until the end of your next turn, but you can Sustain it up to 1 minute. The first time you Sustain the impulse each round, the weeping willow attacks again, dealing @Damage[floor(@actor.level/4)d8[slashing]|options:area-damage] damage to all enemies in the area with a basic reflex save. If you use this impulse again, the previous one ends.

**Level (20th)** The initial damage is 14d8, and the Sustained damage is 5d8.

**Source:** `= this.source` (`= this.source-type`)
