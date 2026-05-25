---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Mental]]", "[[Nonlethal]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Illusory pain wracks the target, dealing 2d4 mental damage and @Damage[(@item.level)d4[persistent,mental]] damage. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target takes full initial damage but no persistent damage, and the spell ends immediately.
- **Failure** The target takes full initial and persistent damage, and the target is [[Sickened]] 1. If the target recovers from being Sickened, the persistent damage ends and the spell ends.
- **Critical Failure** As failure, but the target is [[Sickened]] 2.

**Heightened (+1)** The damage increases by 2d4 and the persistent damage by 1d4.

**Source:** `= this.source` (`= this.source-type`)
