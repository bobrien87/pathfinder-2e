---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Detection]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
duration: "10 minutes"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You open your mind to the metaphysical, enabling you to sense nearby spirits. Even if you aren't [[Searching]], you get a check to find haunts and spirits in the area. You gain a +1 status bonus to the following checks regarding haunts or spirits: Perception checks to [[Seek]], attempts to Recall Knowledge, skill checks to determine the reason for their existence, and skill checks to disable a haunt. You also gain a +1 status bonus to AC and saving throws against haunts and spirits.

**Heightened (6th)** The spell's duration lasts until the next time you make your daily preparations.

> [!danger] Effect: Spell Effect: Spirit Sense

**Source:** `= this.source` (`= this.source-type`)
