---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Arcane]]", "[[Light]]", "[[Magus]]"]
prerequisites: "aloof firmament hybrid study, Spellstrike"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your [[Spellstrike]] is charged, and you're wielding a one-handed weapon in the sword group.

Honed through 10,000 battles, your sword's mere light can shatter ambitions and break armies. Make a melee Spellstrike with a sword, with a spell that isn't a cantrip or focus spell. Countless copies of your sword, made of light, fall around you, dealing damage equal to double the spell's rank to each creature within a @Template[type:emanation|distance:10] of the target, excluding you and the target of the Spellstrike. The damage is of the same type dealt by your sword Strike and is treated as cold iron and silver.

**Source:** `= this.source` (`= this.source-type`)
