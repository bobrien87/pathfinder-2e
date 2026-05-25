---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Kineticist]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Rather than incantations and gestures, you can use your kinetic gate to directly unlock the potential of elementally empowered magic items. You can Activate magic items that require you to be able to [[Cast a Spell]], provided you activate them to Cast a Spell with the same trait as one of your kinetic elements; for example, if you can channel fire, you could Activate a *scroll of* [[Fireball]]. For any effects of these items that use a spell attack roll or spell DC, you can substitute your impulse attack roll or class DC.

You can also prepare a staff that has at least one spell with an appropriate trait, using half your level rounded up to determine the number of charges you add. This doesn't allow you to cast spells without the trait of one of your kinetic elements, and you don't get the extra benefits prepared and spontaneous spellcasters do.

**Source:** `= this.source` (`= this.source-type`)
