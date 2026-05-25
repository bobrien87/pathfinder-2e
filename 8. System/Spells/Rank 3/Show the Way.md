---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Detection]]", "[[Manipulate]]"]
cast: "10 minutes"
area: "20-foot emanation"
duration: "8 hours"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You and allies in the area gain preternatural knowledge of the path ahead, allowing you to intuit the best way forward and avoid potential obstacles, such as difficult or confusing terrain. For the purpose of long-distance overland travel during exploration mode, traveling through difficult terrain reduces you to only three-quarters your travel Speed instead of half, and traveling through greater difficult terrain reduces your travel Speed to only half your travel Speed instead of one-third. Show the way doesn't prevent you from falling into traps or encountering other artificial obstacles and hazards.

**Heightened (6th)** For the purpose of long-distance overland travel during exploration mode, traveling through difficult terrain doesn't reduce your travel Speed at all, and traveling through greater difficult terrain reduces your travel Speed to only three-quarters of its normal value instead of one-third.

**Source:** `= this.source` (`= this.source-type`)
