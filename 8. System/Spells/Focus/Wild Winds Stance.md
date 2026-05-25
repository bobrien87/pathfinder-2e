---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Air]]", "[[Focus]]", "[[Manipulate]]", "[[Monk]]", "[[Stance]]"]
cast: "`pf2:1`"
duration: "until you leave the stance"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You take on the stance of the flowing winds, sending out waves of energy at a distance. You can make wind crash unarmed Strikes as ranged Strikes against targets within 30 feet. These deal 1d6 bludgeoning damage; are in the brawling group; and have the agile, nonlethal, propulsive, and unarmed traits. Wind crash Strikes ignore [[Concealment]] and all cover.

While in *wild winds stance*, you gain a +2 circumstance bonus to AC against ranged attacks.

> [!danger] Effect: Stance: Wild Winds Stance

**Source:** `= this.source` (`= this.source-type`)
