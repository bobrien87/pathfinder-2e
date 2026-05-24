---
type: spell
sub-type: "{Cantrip/Spell/Ritual}"
source-type: "{source-type}"
level: "{level}"
traits: "{traits}"
traditions: "{traditions}"
cast: "{cast}"
range: "{range}"
area: "{area}"
targets: "{targets}"
defense: "{defense}"
duration: "{duration}"
trigger: "{trigger}"
requirements: "{requirements}"
source: "{source}"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traits != null, "<br>**Traits** " + this.traits, "") + choice(this.traditions != null, "<br>**Traditions** " + this.traditions, "")`

***

`= "**Cast** " + this.cast + choice(this.trigger != null, "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null, "<br>**Requirements** " + this.requirements, "") + choice(this.range != null or this.area != null or this.targets != null, "<br>" + choice(this.range != null, "**Range** " + this.range, "") + choice(this.area != null, choice(this.range != null, "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null, choice(this.range != null or this.area != null, "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null or this.duration != null, "<br>" + choice(this.defense != null, "**Defense** " + this.defense, "") + choice(this.duration != null, choice(this.defense != null, "; ", "") + "**Duration** " + this.duration, ""), "")`

***

{description}

{heightened}

**Source:** `= this.source` (`= this.source-type`)
