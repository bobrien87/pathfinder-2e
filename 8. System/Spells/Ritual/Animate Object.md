---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
cast: "1 day"
range: "10 feet"
targets: "1 object"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You transform the target into an animated object with a level up to that allowed by the Creature Creation Rituals table and of a type corresponding to the object (so a broom would become an animated broom).
- **Critical Success** The target becomes an animated object of the appropriate type. If it's at least 4 levels lower than you, you can make it a minion. This gives it the minion trait, meaning it can use 2 actions when you command it, and commanding it is a single action that has the auditory and concentrate traits. You can have a maximum of four minions under your control. If it doesn't become a minion, you can give it one simple command. It pursues that goal single-mindedly, ignoring any of your subsequent commands.
- **Success** As critical success, except an animated object that doesn't become your minion stays in place and attacks anyone that attacks it or tries to steal or move it, rather than following your command.
- **Failure** You fail to create the animated object.
- **Critical Failure** You create the animated object, but it goes berserk and attempts to destroy you.

Creatures Creation RitualsCreature LevelSpell Rank RequiredCost-1 or 0215 gp1260 gp23105 gp33180 gp44300 gp54480 gp65750 gp751,080 gp861,500 gp962,100 gp1073,000 gp1174,200 gp1286,000 gp1389,000 gp14913,500 gp15919,500 gp161030,000 gp171045,000 gp

**Source:** `= this.source` (`= this.source-type`)
