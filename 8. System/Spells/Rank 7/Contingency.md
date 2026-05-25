---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "10 minutes"
duration: "until the next time you make your daily preparations"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You prepare a spell that will trigger later. While casting contingency, you also cast another spell of 4th rank or lower with a casting time of no more than 3 actions. This companion spell must be one that can affect you. You must make any decisions for the spell when you cast contingency, such as choosing a damage type for resist energy. During the casting, choose a trigger under which the spell will be cast, using the same restrictions as for the trigger of a Ready action. Once contingency is cast, you can cause the companion spell to come into effect as a reaction with that trigger. It affects only you, even if it would affect more creatures. If you define complicated conditions, as determined by the GM, the trigger might fail. If you cast contingency again, the newer casting supersedes the older.

**Heightened (8th)** You can choose a spell of 5th rank or lower.

**Heightened (9th)** You can choose a spell of 6th rank or lower.

**Heightened (10th)** You can choose a spell of 7th rank or lower.

**Source:** `= this.source` (`= this.source-type`)
