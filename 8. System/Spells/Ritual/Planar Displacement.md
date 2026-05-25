---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "7"
traits: ["[[Teleportation]]"]
cast: "1 day"
range: "20 feet"
area: "20-foot burst"
requirements: "planar key for the destination plane used as a locus"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You draw a ritual circle, and when the ritual is complete, you shift all creatures in the area to a different plane of existence. The skill you use for the primary check must be one that can be used to make a Recall Knowledge check about the intended destination, such as Arcana or Nature for the Plane of Fire or Occultism for the Astral Plane.

A secondary caster can be located at the exact site of the destination, instead of with you at the point of origin. If a secondary caster at the destination succeeds at its check and you roll a success, the ritual is a critical success instead.
- **Critical Success** You arrive on the intended plane at the last place one of the targets (of your choice) was located the last time the target traveled to that plane. If it's the first time traveling to a particular plane for all targets, you appear at a random location on the plane. The circle remains active for 1 minute, during which time any creature the ritual transported can return to the origin point with a single action, which has the concentrate trait.
- **Success** As critical success, but you arrive 1d10×25 miles from your destination.
- **Failure** Your attempt is unsuccessful.
- **Critical Failure** The ritual fails, and the GM determines whether you travel to the wrong plane or are barred from planar travel for 1 week.

**Source:** `= this.source` (`= this.source-type`)
