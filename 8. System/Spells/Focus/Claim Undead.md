---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Oracle]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 undead creature"
defense: "Will"
duration: "10 minutes"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You attempt to wrest control of a target undead or force it to recognize you as its master. If the target is controlled by another creature, that controller attempts a Will saving throw to retain control; otherwise, the target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Stunned]] 1 and [[Confused]] for 1 round as it fights off your commands.
- **Failure** The target becomes controlled by you and follows your orders. It (or the creature previously controlling it) can attempt a new Will save at the end of each of its turns; on a success, the spell ends, and the creature becomes stunned 1 and confused for 1 round. If you issue an obviously self-destructive order, the target doesn't act until you issue a new order.
- **Critical Failure** As failure, but the target (or the creature previously controlling it) receives a new save only if you give it a new order that is against its nature.

**Source:** `= this.source` (`= this.source-type`)
