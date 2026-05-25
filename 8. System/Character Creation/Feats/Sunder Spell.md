---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Attack]]", "[[Barbarian]]", "[[Concentrate]]", "[[Rage]]"]
prerequisites: "superstition instinct"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You draw upon your superstitious fury to destroy a spell. Make a melee Strike with a weapon or unarmed attack against a creature, object, or a spell manifestation (such as the wall created by [[Wall of Fire]] or the guardian from [[Spiritual Guardian]]). If you're targeting something that doesn't have an AC listed, its AC against this Strike is usually 10 for targets that are very easy to hit, like a wall, or a different AC determined by the GM. If your Strike hits, you can attempt to counteract a single spell or magical effect on the target. Your counteract rank for this attempt is equal to half your level rounded up, and you use the result of your attack roll for the counteract check.

Whether or not you succeed at your Strike, the target becomes temporarily immune to your Sunder Spell for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
