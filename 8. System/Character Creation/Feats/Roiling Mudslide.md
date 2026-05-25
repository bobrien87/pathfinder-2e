---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Composite]]", "[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You form water and earth into a mudslide that smashes your opponents and coats them in mud. Each creature in a @Template[cone|distance:30] takes @Damage[(floor((@actor.level -6)/4)+2)d8[bludgeoning]|options:area-damage] damage with a [[Fortitude]] save against your class DC. A creature that fails is also pushed 5 feet (or 10 feet on a critical failure) and coated in mud until the end of its next turn. While coated in mud, the creature falls [[Prone]] at the end of its movement any time it ends a move action other than a [[Crawl]] or Step. The creature can attempt an Acrobatics check or [[Reflex]] save against your class DC, avoiding the fall if it succeeds.

**Level (+4)** The damage increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
