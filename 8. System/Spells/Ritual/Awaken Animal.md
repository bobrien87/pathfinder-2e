---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "6"
traits: ["[[Mental]]"]
cast: "1 day"
range: "10 feet"
targets: "1 animal up to the level on the table"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You grant intelligence to the target, transforming it into a beast. If it was previously an animal companion or minion, it can no longer serve as one.
- **Critical Success** The target's Intelligence, Wisdom, and Charisma modifiers each increase to +2 if they were lower, and it becomes helpful to you for awakening it.
- **Success** The target's Intelligence, Wisdom, and Charisma modifiers increase to +0 if they were lower and it becomes friendly to you for awakening it.
- **Failure** You fail to awaken the target.
- **Critical Failure** You accidentally awaken the target with a pure bestial hatred toward you. The target's Intelligence, Wisdom, and Charisma modifiers increase to -2 if they were lower. It becomes hostile to you, attempting to destroy you.

Creatures Creation RitualsCreature LevelSpell Rank RequiredCost-1 or 0215 gp1260 gp23105 gp33180 gp44300 gp54480 gp65750 gp751,080 gp861,500 gp962,100 gp1073,000 gp1174,200 gp1286,000 gp1389,000 gp14913,500 gp15919,500 gp161030,000 gp171045,000 gp

**Source:** `= this.source` (`= this.source-type`)
