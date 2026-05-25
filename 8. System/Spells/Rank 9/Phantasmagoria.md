---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Death]]", "[[Illusion]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "any number of creatures"
defense: "Will"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You fill the targets' minds with endless images, like countless dreams and lives colliding with each other. The onrushing information deals 16d6 mental damage to each target, depending on its Will save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage and can't use reactions until the start of your next turn.
- **Failure** The target takes full damage and is [[Confused]] until the start of your next turn.
- **Critical Failure** The target takes double damage and is confused for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
