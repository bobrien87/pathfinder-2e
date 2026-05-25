---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
defense: "Will"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You afflict the target with the curse of the roiling, unforgiving sea. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target becomes [[Sickened]] 1. Reducing its sickened condition to 0 ends the curse.
- **Failure** The target becomes sickened 1 and can't reduce its sickened condition below 1 while the curse remains. The curse can be lifted by 4th-rank [[Cleanse Affliction]] or similar magic. Whenever the target is sickened and on the water at least a mile from shore, it is also [[Slowed]] 1.
- **Critical Failure** As failure, but the target becomes [[Sickened]] 2.

**Source:** `= this.source` (`= this.source-type`)
