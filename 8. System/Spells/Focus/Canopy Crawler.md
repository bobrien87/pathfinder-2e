---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Morph]]", "[[Ranger]]"]
cast: "`pf2:2`"
range: "touch"
targets: "yourself or your animal companion"
duration: "10 minutes"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The target grows a prehensile tail, or gains prehensile qualities in their existing tail, to help them climb with ease. For the duration of the spell, they gain a climb Speed equal to their highest Speed. The target can Climb with a hand occupied (or two hands occupied if they have the [[Combat Climber]] feat).

> [!danger] Effect: Spell Effect: Canopy Crawler

**Heightened (5th)** The spell's duration increases to 1 hour, and you can target both yourself and your animal companion with a single casting.

**Source:** `= this.source` (`= this.source-type`)
