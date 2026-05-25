---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "10 minutes"
range: "30 feet"
targets: "one creature"
duration: "8 hours"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a Large fantastical creature to serve as a mount for the target. The mount is the target's minion, has a Speed of 40 feet, and can bear the target with any carried possessions. It can't carry any other creature. The mount uses the target's AC and saves, but it's destroyed if it takes more than 10 damage at one time, ending the spell.

**Heightened (3rd)** The mount can walk on water, but it must end its turn on solid ground or sink.

**Heightened (4th)** The mount has a Speed of 60 feet and can walk on water.

**Heightened (5th)** The mount has a Speed of 60 feet and can walk on water. It also has a fly Speed of 60 feet, but it must end its turn on a surface or fall.

**Heightened (6th)** The mount has a Speed and fly Speed of 80 feet.

**Source:** `= this.source` (`= this.source-type`)
