---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a barrier of gusting winds that hinders anything moving through it. The wall of swirling winds is 5 feet thick, 60 feet long, and 30 feet high. The wall stands vertically, but you can shape its path. Though the wall of wind distorts the air, it does not hamper sight. The wall has the following effects.

- Ammunition from physical ranged attacks-such as arrows, bolts, sling bullets, and other objects of similar size-can't pass through the wall. Attacks with bigger ranged weapons, such as javelins, take a -2 circumstance penalty to their attack rolls if their paths pass through the wall. Massive ranged weapons and spell effects that don't create physical objects pass through the wall with no penalty.

- The wall is difficult terrain to creatures attempting to move overland through it. Gases, including creatures in [[Vapor Form]], can't pass through the wall.

- A creature that attempts to fly through the wall using a move action must attempt a Fortitude save.
- **Critical Success** The creature can move through the wall normally this turn.
- **Success** The flying creature can move through the wall this turn, but the wall is difficult terrain.
- **Failure** The wall stops the movement of the flying creature, and any remaining movement from its current action is wasted.
- **Critical Failure** As failure, and the creature is pushed 10 feet away from the wall.

**Source:** `= this.source` (`= this.source-type`)
