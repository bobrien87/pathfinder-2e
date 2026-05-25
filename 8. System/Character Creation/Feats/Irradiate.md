---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Deviant]]", "[[Magical]]", "[[Poison]]"]
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You exude an aura of radiation, making everyone around you ill. All creatures in a @Template[emanation|distance:15] must succeed at a [[Fortitude]] save or become [[Sickened]] 1. On a critical failure, they're also [[Fatigued]] for 1 minute. You're immune to your own radiation. The value of this sickened condition increases by 1 for every 5 levels you have beyond 6th.

**Awakening** You become more efficient at exuding this aura of radiation. The radius of the emanation becomes @Template[emanation|distance:60]{60 feet}.

**Awakening** Your radiation becomes more potent. Creatures in the area take an additional @Damage[(floor(@actor.level/2))d4[poison]|options:area-damage]{1d4 poison} damage for every 2 levels you have, with a [[Fortitude]] save (roll this Fortitude save once and apply it to both the damage and the sickened condition).

**Source:** `= this.source` (`= this.source-type`)
