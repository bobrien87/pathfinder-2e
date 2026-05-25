---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The landscape fills with monumental filaments of metal. The needles lance into a cube 30 feet on a side within 500 feet. Each creature in the area takes @Damage[(ternary(gte(@actor.level,20),17,13))d6[piercing]|options:area-damage] damage, with a [[Reflex]] save against your class DC. Each creature that fails its save is impaled, becoming [[Immobilized]] until it [[Escapes]] (the DC is your class DC); a creature that critically failed is also off-guard as long as it's impaled. The hell remains until the end of your next turn, but you can Sustain it up to 1 minute. Using this impulse again ends any previous one. The first time you Sustain it each round, lightning crisscrosses the needles. Each creature in the area takes @Damage[3d12[electricity]|options:area-damage] damage with a [[Reflex]] save against your class DC. Squares in the area are hazardous terrain. A creature takes @Damage[(ternary(gte(@actor.level,20),7,6))[piercing]] damage for every square of the area it moves through.

**Level (20th)** The initial damage is 17d6, and the hazardous terrain damage is 7.

**Source:** `= this.source` (`= this.source-type`)
