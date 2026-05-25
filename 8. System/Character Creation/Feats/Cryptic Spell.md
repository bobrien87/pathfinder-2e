---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Druid]]", "[[Spellshape]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're in natural terrain.

You hide your magic in the croak of a frog, in the sway of the trees, in the howl of the wind, and the flicker of the will-o'-wisp. If the next action you take is to Cast a Spell, the spell gains the subtle trait, masking the spell's manifestations in the natural sights and sounds of the environment.

The trait hides only the spell's spellcasting actions and manifestations, not its effects, so an observer might still see you transform into a giant bear.

**Source:** `= this.source` (`= this.source-type`)
