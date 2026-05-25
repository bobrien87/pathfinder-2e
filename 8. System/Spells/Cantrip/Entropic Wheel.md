---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Cantrip]]", "[[Cold]]", "[[Concentrate]]", "[[Fire]]", "[[Psychic]]"]
cast: "`pf2:r`"
duration: "1 minute"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You deal cold or fire damage to an enemy.

You stockpile thermal energy in a magical wheel-like construct that lets you burn opponents with cold or freeze their bodies with heat. When you Cast the Spell, the wheel has one mote of thermal energy, and when you use a cold or fire effect or deal cold or fire damage, the wheel spins, siphoning off a bit of energy and gaining another mote. The wheel can't gain motes more than once on a given turn, and the maximum number of motes is equal to *entropic wheel*'s rank.

When you Cast a Spell that deals fire damage, the target also takes cold damage equal to the number of motes in the *entropic wheel*. When you Cast a Spell that deals cold damage, the target also takes fire damage equal to the number of motes in the *entropic wheel*. This applies only to the initial damage of the spell, not to any persistent damage or ongoing effects.

> [!danger] Effect: Spell Effect: Entropic Wheel

**Source:** `= this.source` (`= this.source-type`)
