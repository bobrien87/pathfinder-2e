---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Focus]]", "[[Magus]]", "[[Manipulate]]"]
cast: "`pf2:1`"
requirements: "You're wielding qi-infused fabric."
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Requirements** You're wielding qi-infused fabric.

Qi-formed threads unravel from your fabric on conjured needles as your attack makes contact with an enemy and wraps it in place like an insect in its cocoon. Make a melee Strike with your qi-infused fabric. On a success, the target is [[Immobilized]] until the start of your next turn, though it can attempt to [[Escape]] against your spell DC. On a critical success, your needles anchor in the target's nerve centers after the threads bind it, making it your choice of [[Clumsy]] 1 or [[Enfeebled]] 1 until the start of your next turn, in addition to immobilizing it.

**Source:** `= this.source` (`= this.source-type`)
