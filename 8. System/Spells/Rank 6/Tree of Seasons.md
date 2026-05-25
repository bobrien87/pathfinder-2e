---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:2`"
range: "60 feet"
defense: "basic Reflex"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause a Small tree to instantly sprout in an unoccupied space on the ground. Four seedpods grow from the tree, each filled with the magic of a different one of the four seasons. A creature can Interact to pluck one of the pods, and can then either throw it up to 30 feet as part of the same action or do so with a separate Interact action later. When thrown, a pod explodes in a @Template[burst|distance:5], dealing 6d6 damage with a basic Reflex save against your spell DC. The damage type depends on the season of the pod: electricity for spring, fire for summer, poison for autumn, or cold for winter. When the spell ends, the tree withers away and any remaining pods rot, leaving behind non-magical seeds.

@Damage[(@item.level)d6[cold]]

@Damage[(@item.level)d6[electricity]]

@Damage[(@item.level)d6[fire]]

@Damage[(@item.level)d6[poison]]

**Heightened (+1)** The burst's damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
