---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Focus]]", "[[Polymorph]]"]
cast: "`pf2:1`"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your apparition casts a feral shadow over your form. You can polymorph into any form listed in [[Pest Form]]. When you transform into a form granted by a spell, you gain all the effects of the form you chose from a version of the spell heightened to darkened forest form's rank. Each time you Sustain this Spell, you can choose to change to a different shape from those available via any of the associated spells.

**Heightened (2nd)** You can also transform into the forms listed in [[Animal Form]].

**Heightened (5th)** You can also transform into the forms listed in [[Elemental Form]].

**Source:** `= this.source` (`= this.source-type`)
