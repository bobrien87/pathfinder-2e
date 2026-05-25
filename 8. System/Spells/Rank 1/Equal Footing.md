---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature with a land Speed greater than yours"
defense: "Will"
duration: "varies"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You level the field between yourself and another creature, hampering its movements if it's quicker than you. The target attempts a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Clumsy]] 1 and takes a –10-foot status penalty to all its Speeds until the end of your next turn.

> [!danger] Effect: Spell Effect: Equal Footing (Success)
- **Failure** The target is clumsy 1 and takes a –15-foot status penalty to all its Speeds for 1 minute. During this time, it can't benefit from bonuses to its Speeds or take other penalties to its Speeds.
- **Critical Failure** The target is [[Clumsy]] 2 and takes a –15-foot status penalty to all its Speeds for 1 minute. During this time, it can't benefit from bonuses to its Speeds or take other penalties to its Speeds.

> [!danger] Effect: Spell Effect: Equal Footing (Failure or Critical Failure)

**Source:** `= this.source` (`= this.source-type`)
