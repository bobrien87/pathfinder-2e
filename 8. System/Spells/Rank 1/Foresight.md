---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ""
traditions: ""
cast: ""
range: ""
area: ""
targets: ""
defense: ""
duration: ""
trigger: ""
requirements: ""
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traits != null, "<br>**Traits** " + this.traits, "") + choice(this.traditions != null, "<br>**Traditions** " + this.traditions, "")`

`= "**Cast** " + this.cast + choice(this.trigger != null, "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null, "<br>**Requirements** " + this.requirements, "") + choice(this.range != null or this.area != null or this.targets != null, "<br>" + choice(this.range != null, "**Range** " + this.range, "") + choice(this.area != null, choice(this.range != null, "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null, choice(this.range != null or this.area != null, "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null or this.duration != null, "<br>" + choice(this.defense != null, "**Defense** " + this.defense, "") + choice(this.duration != null, choice(this.defense != null, "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** The target of [[Foresight]] defends against a hostile creature or other danger.

**Effect** If the hostile creature or danger forces the target to roll dice (a saving throw, for example), the target rolls twice and uses the higher result, and this spell gains the fortune trait. But if the hostile creature or danger is rolling against the target (an attack roll or skill check, for example), that hostile creature or danger rolls twice and uses the lower result, and this spell gains the misfortune trait.

**Source:** `= this.source` (`= this.source-type`)
