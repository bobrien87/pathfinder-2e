---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "1 minute"
range: "touch"
targets: "1 stone of at least 1 Bulk"
duration: "unlimited"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You store memories inside a stone. This memory can convey up to 10 minutes of material. When you Cast this Spell, choose a command word. Doing so creates a carved symbol on the stone that hints at the word. Any creature can access the memories stored within the stone by using an action to speak the command word.

As it imparts the memories, the stone crumbles to dust, but the memory is infallibly available to the creature that activated the stone for the next 24 hours. After that time, the creature's normal capacity for memory must be relied upon to recall the stone's imparted memory. It's up to the GM what benefit the imparted memory grants, from circumstance bonuses to checks related to the memory or clear information on subjects the memory covers.

**Source:** `= this.source` (`= this.source-type`)
