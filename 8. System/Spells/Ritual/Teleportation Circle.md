---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "7"
traits: ["[[Teleportation]]"]
cast: "1 day"
range: "20 feet"
duration: "1 day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a 10-foot-diameter circle on the ground, which acts as a portal to a destination determined at the time of the ritual. You designate the destination of the teleportation as part of the ritual. This destination can't be changed. The destination must be a location within 1,000 miles and be on the same plane as the teleportation circle. You must be able to identify the location precisely both by its position relative to the location where you create the teleportation circle and by the destination's appearance (or other identifying features). The destination must also be a 10-foot-diameter circle that doesn't overlap with any solid structures, but it can be a place that is harmful or dangerous.

A secondary caster attempting a Survival check for this ritual can be located at the destination, instead of at the point of origin. If the secondary caster succeeds at their check at the destination and you roll a success, the ritual is a critical success instead.

While the circle is active, any creature that moves to be fully within the circle is instantly teleported to the destination. A creature that is unwilling to be teleported can attempt a Will save to resist the effect. If it remains in the circle, the creature must attempt this save again at the end of each of its turns.

The circle normally works only in one direction, though you can double the cost to make it work in both directions.
- **Critical Success** You create the teleportation circle, and it's extremely precise, regardless of the distance traveled. Travelers arrive exactly at the designated point.
- **Success** As a critical success, but the destination is off target by roughly 1 percent of the distance traveled, to a maximum of 10 miles off target.
- **Failure** The teleportation circle doesn't function.
- **Critical Failure** The teleportation circle is wildly inaccurate. It leads to a random destination roughly the same distance from the origin point, and the chances of some other unusual mishap are much greater.

**Heightened (9th)** The cost is 2,000 gp, the duration is 1 month, and the destination can be anywhere on the same planet.

**Heightened (10th)** The cost is 10,000 gp, the duration is unlimited, and the destination can be anywhere on the same planet

**Source:** `= this.source` (`= this.source-type`)
