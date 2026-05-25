---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 object"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You place a hand on an object to learn a piece of information about an emotional event that occurred involving the object within the past week, determined by the GM. If you cast *object reading* on the same item multiple times, you can either concentrate on a single event to gain additional pieces of information about that event, or you can gain a piece of information about another emotional event in the applicable time frame.

**Heightened (2nd)** You can learn about an event that occurred within the last month.

**Heightened (4th)** You can learn about an event that occurred within the last year.

**Heightened (6th)** You can learn about an event that occurred within the last decade.

**Heightened (8th)** You can learn about an event that occurred within the last century.

**Heightened (9th)** You can learn about an event that occurred within the entirety of the object's history.

**Source:** `= this.source` (`= this.source-type`)
