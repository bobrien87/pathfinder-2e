---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
cast: "1 day"
duration: "1 year"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 100 feet × 100 feet, up to 20 feet high

You create a long-lasting adaptation of the [[Phantasmal Minion]], forming entities to carry out basic tasks at a fixed location.
- **Critical Success** The ritual creates six *phantasmal minions*. You don't need to concentrate on them, and they aren't summoned minions. You can spend an action, which has the concentrate trait, to command one to perform a basic task; it continues to perform the task until commanded again.
- **Success** As critical success, but the ritual creates three minions.
- **Failure** The ritual fails to create any *phantasmal minions*.
- **Critical Failure** The ritual creates six *phantasmal minions*, but these creatures are hostile and capable of making fist Strikes with an attack bonus equal to your skill modifier for the primary skill check, dealing 1d6 force damage. They attack you and your allies and attempt to break objects belonging to you and your allies within the area.

**Heightened (6th)** If destroyed, the *phantasmal minions* reform the next morning. The cost increases to 30 gp

**Source:** `= this.source` (`= this.source-type`)
