---
type: action
source-type: "Remaster"
traits: ["[[Primal]]", "[[Sonic]]"]
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** Your animal companion screeches and howls, empowered with natural magic. All creatures in a @Template[cone|distance:30] take @Damage[(floor(@actor.level/2))d6[sonic]|options:area-damage] damage for every 2 levels your companion has, with a [[Fortitude]] save against your spell DC. Creatures that fail become [[Frightened]] 1, and creatures that critically fail become [[Frightened]] 2. The fright is an emotion, fear, and mental effect.

**Source:** `= this.source` (`= this.source-type`)
