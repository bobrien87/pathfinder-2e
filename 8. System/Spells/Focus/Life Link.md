---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Focus]]", "[[Healing]]", "[[Manipulate]]", "[[Oracle]]", "[[Vitality]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature other than you"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You forge a connection of life energy between you and your target, distributing harm between both of you. When you first Cast the Spell, the target recovers 1d4 Hit Points.

The first time each round that the target takes damage, reduce the damage it takes by 3 (to a minimum of 0 damage). You lose 3 Hit Points each time, or the total damage dealt, if less than 3; this damage ignores any immunities or resistances you have and can't otherwise be mitigated in any way.

The spell ends immediately if you fall [[Unconscious]]. You can Dismiss the spell.

**Heightened (3rd)** You can target 2 creatures other than you. The initial healing increases to 3d4 Hit Points and the maximum damage reduced and Hit Points lost increases to 5.

**Heightened (6th)** You can target 3 creatures other than you. The initial healing increases to 6d4 Hit Points and the maximum damage reduced and Hit Points lost increases to 10.

**Heightened (9th)** You can target 4 creatures other than you. The initial healing increases to 9d4 Hit Points and the maximum damage reduced and Hit Points lost increases to 15.

**Source:** `= this.source` (`= this.source-type`)
