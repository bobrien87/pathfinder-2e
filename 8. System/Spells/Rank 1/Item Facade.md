---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 object no more than 10 feet by 10 feet by 10 feet"
duration: "1 hour"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You make the target object look and feel as though it were in much better or worse physical condition. When you cast this spell, decide whether you want to make the object look decrepit or perfect. An item made to look decrepit appears [[Broken]] and shoddy. An intact item made to look better appears as though it's brand new and highly polished or well maintained. A Broken item appears to be intact and functional. Destroyed items can't be affected by this spell. A creature that Interacts with the item can attempt to disbelieve the illusion.

**Heightened (2nd)** The duration is 24 hours.

**Heightened (3rd)** The duration is unlimited.

**Source:** `= this.source` (`= this.source-type`)
