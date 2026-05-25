---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With an upward gesture, you shape a vertical column of extreme heat. The cylinder is @Template[cylinder|distance:5]{10 feet in diameter} and 30 feet high, and the bottom must be within 60 feet of you. Each creature in the area takes @Damage[(floor((@actor.level -1)/3)+1)d6[fire]|options:area-damage] damage with a [[Reflex]] save against your class DC.

The flame remains briefly, making all squares in the column hazardous terrain until the end of your next turn, and you can Sustain the impulse up to 1 minute. A creature takes @Damage[(2*floor((@actor.level -1)/3)+1)[fire]] damage each time it moves into one of these squares.

**Level (+3)** The initial damage increases by 1d6, and the hazardous terrain damage increases by 2.

**Source:** `= this.source` (`= this.source-type`)
