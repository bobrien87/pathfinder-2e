---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature or unattended object"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call forth a powerful blast of pressurized water that bludgeons the target and knocks it back. Make a ranged spell attack roll.
- **Critical Success** The target takes 6d6 bludgeoning damage and is knocked back 10 feet.
- **Success** The target takes 3d6 bludgeoning damage and is knocked back 5 feet.

**Heightened (+1)** The bludgeoning damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
