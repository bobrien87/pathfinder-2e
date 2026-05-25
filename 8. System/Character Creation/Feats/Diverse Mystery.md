---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Oracle]]"]
prerequisites: "Advanced Revelation"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have broadened your understanding of the divine and can tap into the wonders of a different mystery. Select one revelation spell from a mystery other than your own. You can choose only an initial revelation spell or an advanced revelation spell.

This spell gains the cursebound trait for you, and when you cast it, you gain the [[Cursebound 1]] effects of its mystery in addition to your normal curse effects. Any ability that lets you use a cursebound ability without increasing the severity of your curse also prevents you from gaining this additional curse effect.

You can't cast your chosen revelation spell if any of the following conditions are true:

- its mystery's curse effects directly conflict with or negate the effects of your own mystery's curse,

- the curse would have no effect on you (for example, removing an ability from your original mystery that you lack),

- or if either of these criteria would be met once you finish Casting the Spell

**Source:** `= this.source` (`= this.source-type`)
