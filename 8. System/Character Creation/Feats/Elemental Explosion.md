---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Barbarian]]", "[[Concentrate]]", "[[Primal]]", "[[Rage]]"]
prerequisites: "elemental instinct"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're raging, and you haven't used this ability since you last Raged.

You unleash the energy roiling within you, exploding elemental matter in a @Template[emanation|distance:15]. Each creature in the area takes @Damage[(@actor.level)d8[@actor.flags.system.elementalInstinctDamage]|options:area-damage]{1d8 damage per level you possess}, with the same type you chose for elemental rage. Each creature in the area must attempt a [[Reflex]] save. Elemental Explosion gains the trait of your element.

**Source:** `= this.source` (`= this.source-type`)
