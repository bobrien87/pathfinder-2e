---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Air]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "10-foot emanation"
defense: "basic Fortitude"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You rapidly draw the air from your surroundings, hoarding it for yourself. Creatures in the area when the spell is cast take 5d6 bludgeoning damage with a basic Fortitude save. A creature that fails its save can't speak above a raspy whisper for 1 round. A creature that critically fails can't speak or use abilities that require it to breathe for 1 round. This prevents it from using effects that require speech, such as casting spells with verbal components, and from using a breath weapon or similar ability.

Creatures made of air (such as air elementals) attempting a save against this spell get a degree of success one worse than they rolled.

**Heightened (+1)** Increase the damage by 2d6.

**Source:** `= this.source` (`= this.source-type`)
