---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Animist]]", "[[Concentrate]]", "[[Spellshape]]", "[[Witch]]", "[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Animist** You speak with the unheard voice of the spirits.

**Witch** Through sheer mental effort, you can simplify the incantations and gestures needed to spellcast, leaving them barely noticeable.

**Wizard** By shaping the magical energies and parameters of your spells all in your head through sheer concentration, you can simplify the incantations and gestures needed to spellcast, leaving them barely noticeable.

If the next action you use is to Cast a Spell, the spell gains the subtle trait, hiding the shining runes, sparks of magic, and other manifestations that would usually give away your spellcasting. The trait hides only the spell's spellcasting actions and manifestations, not its effects, so an observer might still see a ray streak out from you or see you vanish into thin air.

**Source:** `= this.source` (`= this.source-type`)
