---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Air]]", "[[Manipulate]]", "[[Move]]"]
cast: "`pf2:r`"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** A creature enters a space within 5 feet of you.

An arresting breeze sweeps you up in an instant and moves you to safety. You Fly 15 feet directly away from the triggering creature.

**Heightened (6th)** You and one adjacent ally Fly up to 25 feet directly away from the triggering creature.

**Heightened (8th)** You and up to 5 allies within 30 feet Fly up to 25 feet directly away from the triggering creature.

**Source:** `= this.source` (`= this.source-type`)
