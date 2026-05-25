---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wild Mimic|Wild Mimic]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Primal]]", "[[Sonic]]"]
prerequisites: "Wild Mimic Dedication, you have been targeted by a creature's auditory ability that affects an area or have identified a creature with an auditory ability that affects an area"
frequency: "once per PT10M"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You unleash a roar so loud that it's felt as deeply as it's heard. All creatures within a @Template[emanation|distance:15] take @Damage[(max(8,(floor(@actor.level/2)*2)-4))d6[sonic]|options:area-damage] damage and must attempt a [[Fortitude]] save against the higher of your class DC or spell DC. This damage increases by 2d6 at 14th level and every 2 levels thereafter.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Stunned]] 1. If the creature is adjacent to you, they're also [[Deafened]] for 1 round.
- **Critical Failure** The creature takes double damage and is [[Stunned]] 2. If the creature is adjacent to you, they're also deafened for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
