---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Manipulate]]", "[[Teleportation]]"]
cast: "`pf2:1`"
range: "120 feet"
targets: "1 willing creature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You teleport one object of light or negligible Bulk held in your hand to the target. The object appears instantly in the target's hand if they have a free hand, or at their feet if they don't. The target knows what object you're attempting to send them. If the target is [[Unconscious]] or refuses to accept your gift, or if the spell would teleport a creature (even if the creature is inside an extradimensional container), the spell fails.

**Heightened (3rd)** The spell's range increases to 500 feet.

**Heightened (5th)** As 3rd rank, and the object's maximum Bulk increases to 1. You can Cast the Spell with 3 actions instead of 1; doing so increases the range to 1 mile, and you don't need line of sight to the target, but you must be extremely familiar with the target.

**Source:** `= this.source` (`= this.source-type`)
