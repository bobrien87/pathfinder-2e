---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "1 minute"
range: "10 feet"
duration: "1 hour"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You pull earthen material out of the environment, then shape it into one or more earthenware objects that, in combination, can be up to light Bulk. Alternatively, you can cast this spell on objects previously created with this spell, extending their duration. No object can have intricate artistry or complex moving parts, can fulfill a cost or the like, or is made of anything more than clay or earth. Each object is obviously the product of temporary magic and thus can't be sold or passed off as a valuable item.

**Heightened (2nd)** You can create objects of up to 1 Bulk. They last 8 hours.

**Heightened (3rd)** You can create objects of up to 2 Bulk. They last 24 hours.

**Source:** `= this.source` (`= this.source-type`)
