---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Extradimensional]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
duration: "sustained"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You transport the target into an extraplanar puzzle room of mysterious origin, locking them there. Once each turn as a single action, the target can attempt an Occultism check, Perception check, or Thievery check against your spell DC to solve the puzzle. Teleportation effects can't carry the target outside the puzzle room unless they can also traverse the planes, such as [[Interplanar Teleport]]. When the spell ends, the target returns to the space it occupied when it was banished, or to the nearest space if the original is now filled.
- **Critical Success** The target solves the puzzle and escapes.
- **Success** The target is on the right path to the solution. If it was already on the right path, it solves the puzzle and escapes.
- **Failure** The target makes no progress toward a solution.
- **Critical Failure** The target makes no progress and, if it was on the right path, it no longer is.

**Source:** `= this.source` (`= this.source-type`)
