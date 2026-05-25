---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:2`"
range: "60 feet"
defense: "Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A sphere of water 10 feet in diameter forms in an unoccupied space in range, either on the ground or on the surface of a liquid.

When you Cast this Spell and each time you Sustain it, you can roll the orb, moving it up to 10 feet along the ground or the surface of a liquid.

The orb can move through the spaces of any creatures or obstacles that wouldn't stop the flow of water. It extinguishes non-magical fires it moves through of its size or smaller, and it attempts to counteract any magical fires it moves through. If it fails to counteract a given fire, it can't counteract that fire for the duration of the spell.

The orb can engulf Large or smaller creatures it moves through, and it can contain as many creatures as fit in its space. The orb can try to engulf the same creature only once per turn, even if you roll it onto a creature's space more than once. Any Large or smaller creature whose space the orb tries to move through can attempt a Reflex save.
- **Success** The creature can either let the orb pass (remaining in its space or moving out of the orb's path into a space of the creature's choice) or allow itself to be pushed in front of the orb to the end of the orb's movement.
- **Failure** The creature is engulfed in the orb. It moves along with the orb and must hold its breath or begin suffocating (unless it can breathe in water). An engulfed Medium or smaller creature and anyone trying to affect that creature follow the normal rules for aquatic battles. An engulfed Large creature is usually big enough that parts of it stick out from the water, and it can reach out of the water. The creature can get free either by Swimming with a successful [[Athletics]] check or by [[Escaping]] against your spell DC. A freed creature exits the orb's space and can immediately breathe.
- **Critical Failure** As failure, but the creature can't Swim to get free.

**Source:** `= this.source` (`= this.source-type`)
