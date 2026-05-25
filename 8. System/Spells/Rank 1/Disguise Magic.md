---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]"]
cast: "1 minute"
range: "30 feet"
targets: "1 item or spell effect"
duration: "until your next daily preparations"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You alter how an item's or spell's magical aura appears to effects like detect magic. You can hide the auras entirely, have an item register as a common item of lower level, or make a spell register as a common spell of the same or lower rank. You can Dismiss the spell. A caster using [[Detect Magic]] or [[Read Aura]] of a higher rank than disguise magic can attempt to disbelieve the illusion using the skill matching the tradition of the spell (Arcana for arcane, Religion for divine, Occultism for occult, or Nature for primal). Further attempts by the same caster get the same result as the initial check to disbelieve.

**Heightened (2nd)** You can Cast this Spell on a creature, disguising all items and spell effects on it.

**Source:** `= this.source` (`= this.source-type`)
