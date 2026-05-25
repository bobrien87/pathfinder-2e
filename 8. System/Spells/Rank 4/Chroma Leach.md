---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 living creature"
defense: "Fortitude"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your hand glows with impossible colors from beyond the stars, and your touch saps both color and vitality from the living. The target must attempt a Fortitude save; creatures with the gnome trait take a –2 circumstance penalty to this save.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Enfeebled]] 2 for 1 round.
- **Failure** The target is enfeebled 2 for 1 minute and [[Drained]] 1. The target is also filled with listlessness and ennui. For 1 round, if the target tries to use a move action, it must succeed at a Will save against your spell DC or the action is lost; this effect has the mental and emotion traits.
- **Critical Failure** As failure, but the creature is permanently enfeebled 2 and [[Drained]] 2 (although magic such as [[Sound Body]] can remove these conditions).

**Source:** `= this.source` (`= this.source-type`)
