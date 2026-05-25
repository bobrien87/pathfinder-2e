---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You touch a willing creature, causing its skin to harden and form spiky protrusions. The target gains resistance 4 to all physical damage (except adamantine).

> [!danger] Effect: Spike Skin

Whenever a creature damages the target with an unarmed attack or non-reach melee weapon, the attacking creature takes @Damage[(max(2,floor((@actor.level -8)/2)*2+2))[piercing]] damage.

This impulse lasts for 10 minutes, but each time the target takes physical damage, the duration decreases by 1 minute. The target is temporarily immune to this impulse for 1 hour. If you use Spike Skin again, any previous one ends.

**Level (+2)** The resistance and damage each increase by 2.

**Source:** `= this.source` (`= this.source-type`)
