---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Poison]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
defense: "Fortitude"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You magically duplicate a spider's venomous sting. You deal 1d4 piercing damage to the touched creature and afflict it with spider venom. The target must attempt a Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target takes 1d4 poison damage.
- **Failure** The target is afflicted with spider venom at stage 1.
- **Critical Failure** The target is afflicted with spider venom at stage 2.

**Spider Venom** (poison)

**Level** 1

**Maximum Duration** 4 rounds

**Stage 1** 1d4 poison damage and [[Enfeebled]] 1 (1 round)

**Stage 2** 1d4 poison damage and [[Enfeebled]] 2 (1 round)

**Source:** `= this.source` (`= this.source-type`)
