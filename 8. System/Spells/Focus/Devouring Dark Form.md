---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Focus]]", "[[Morph]]"]
cast: "`pf2:1`"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your apparition's dark power blends with your physical body, allowing you to take on terrifying characteristics of creatures that lurk in dark places. Your arms and legs transform into twisting tentacles. You gain a tentacle unarmed attack with 10-foot reach that deals 1d8 bludgeoning damage and has the grapple trait. The first time you Sustain this spell each round, you can attempt a single [[Grapple]] check with your tentacle against a creature within its reach.

> [!danger] Effect: Spell Effect: Devouring Dark Form

**Heightened (2nd)** You can choose to take on the shark battle form from [[Animal Form]] instead of gaining a tentacle unarmed attack, heightened to the same level as this vessel spell. When you do, this spell loses the morph trait and gains the polymorph trait. You can attempt a jaws unarmed Strike against a creature within your reach each time you Sustain this spell.

**Heightened (5th)** You can choose to take on the water elemental battle form from [[Elemental Form]] instead of gaining a tentacle unarmed attack, heightened to the same level as this vessel spell. When you do, this spell loses the morph trait and gains the polymorph trait. You can attempt an unarmed attack Strike against a creature within your reach each time you Sustain this spell.

**Source:** `= this.source` (`= this.source-type`)
