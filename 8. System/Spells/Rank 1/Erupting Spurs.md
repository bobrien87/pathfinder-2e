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
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traits != null, "<br>**Traits** " + this.traits, "") + choice(this.traditions != null, "<br>**Traditions** " + this.traditions, "")`

`= "**Cast** " + this.cast + choice(this.trigger != null, "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null, "<br>**Requirements** " + this.requirements, "") + choice(this.range != null or this.area != null or this.targets != null, "<br>" + choice(this.range != null, "**Range** " + this.range, "") + choice(this.area != null, choice(this.range != null, "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null, choice(this.range != null or this.area != null, "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null or this.duration != null, "<br>" + choice(this.defense != null, "**Defense** " + this.defense, "") + choice(this.duration != null, choice(this.defense != null, "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** A creature takes persistent bleed damage from your bone flense spell

**Effect** You will the bone spurs to erupt in a particularly devastating manner, dealing 6d6 piercing damage (basic Fortitude save) to the triggering creature instead of the persistent bleed damage from bone flense. The duration of bone flense immediately ends.

**Source:** `= this.source` (`= this.source-type`)
