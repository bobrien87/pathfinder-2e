---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "2"
traits: ["[[Teleportation]]"]
cast: "1 hour"
range: "10 feet"
targets: "1 ship no more than 175 feet long"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a link between a ship and an undead member of its crew to temporarily make the ship, and its passengers and crew, as incorporeal as ghosts. The targeted ship must be intact and on or near the surface of some water, and an undead who was a member of the ship's crew in life must be present for the entire ritual.
- **Critical Success** The ship and all creatures aboard it become incorporeal for 1 hour. During this time, the ship can sail at its top speed in any heading chosen by the primary caster, regardless of the winds. The ship can pass through any corporeal obstacles in its path (such as rocks or other vessels), but it must remain in contact with water or the ritual's effects end prematurely. Any skill checks required to sail the ship through rough weather gain a +2 status bonus. A creature that disembarks the ship while the ritual is in effect becomes corporeal again.
- **Success** As critical success, but the status bonus to skill checks is only +1.
- **Failure** The ritual has no effect.
- **Critical Failure** The ship, but not its passengers or crew, becomes incorporeal for 10 minutes, usually resulting in the passengers and crew falling through the ship into the waters below. If the ship was already sailing, it continues in its current direction at its current speed.

**Source:** `= this.source` (`= this.source-type`)
