---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Druid]]", "[[Manipulate]]", "[[Spellshape]]"]
prerequisites: "leaf order"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

If your next action is to Cast a Spell with the fungus or plant trait, a garland of plants grows in a @Template[burst|distance:10] in the spell's range. The plants are difficult terrain and hazardous terrain, covered in your choice of thorns or poisonous vines. Any creature that moves into one of these squares or ends its turn in one takes 2d6 damage (@Damage[(ternary(gte(@actor.level,20),4,ternary(gte(@actor.level,16),3,2)))d6[piercing]|options:area-damage] damage for thorns or @Damage[(ternary(gte(@actor.level,20),4,ternary(gte(@actor.level,16),3,2)))d6[poison]|options:area-damage] for vines). A creature can take this damage only once per turn. You and your familiar are immune to this damage.

The plants last for 1 minute or until you cast another Garland Spell, whichever comes first.

The damage increases to 3d6 at 16th level and 4d6 at 20th level.

**Source:** `= this.source` (`= this.source-type`)
