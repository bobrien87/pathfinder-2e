---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Healing]]", "[[Impulse]]", "[[Kineticist]]", "[[Plant]]", "[[Primal]]", "[[Vitality]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You grow a nourishing nut, vegetable, seed, or fruit. Choose a creature in your kinetic aura. The produce grows in their open hand, or at their feet if they have no open hands. The produce has light Bulk. A creature can eat it with an Interact action to regain @Damage[((floor((max(1,@actor.level)-1)/2)+1)d4+(floor((max(1,@actor.level)-1)/2)*5+1))[vitality,healing]] HP; this is a healing vitality effect. The creature feels full for 10 minutes, during which it has resistance 2 to void damage and can't eat another piece of produce. Produce not consumed by the start of your next turn withers away.

> [!danger] Effect: Fresh Produce

**Level (+2)** The healing increases by 1d4+5, and the resistance increases by 2.

**Source:** `= this.source` (`= this.source-type`)
