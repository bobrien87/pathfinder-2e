---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Fire]]", "[[Impulse]]", "[[Incapacitation]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]", "[[Vitality]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Blinding flames explode in a swirling sphere! The detonation fills a @Template[burst|distance:20] within 60 feet of you. Each creature in the area takes @Damage[(floor((@actor.level -8)/2)+6)d6[fire],(floor((@actor.level -8)/2)+2)d6[vitality]|options:area-damage] damage, and can become [[Dazzled]] or [[Blinded]] depending on the result of its [[Reflex]] save. The light from Solar Detonation is sunlight for creatures with a particular vulnerability to sunlight. Each creature that attempts a save becomes temporarily immune to being dazzled or blinded by Solar Detonation for 10 minutes, but not the impulse's other effects.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is dazzled until the start of your next turn.
- **Failure** The creature takes full damage and is blinded until the start of your next turn.
- **Critical Failure** The creature takes double damage and is blinded for 1 minute.

**Level (+2)** Increase the fire damage by 1d6 and the vitality damage by 1d6.

**Source:** `= this.source` (`= this.source-type`)
