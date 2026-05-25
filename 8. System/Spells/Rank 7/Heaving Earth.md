---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature or object on the ground"
defense: "basic Reflex"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You strike the ground, and unleash a wave that travels through the struck surface to the target. The effect ends as soon as it can't travel through a solid surface, such as a stone floor. Each creature in a line between you and the target is shaken by tremors and must attempt a Reflex saving throw against your spell DC. A creature that fails this save is pushed 10 feet away from you.

The wave explodes once it reaches the target, showering the target with earth and stone and dealing 12d10 bludgeoning damage with a basic Reflex save. A target that fails its save against this explosion is also pushed back 10 feet and knocked [[Prone]]. A creature subject to the explosion doesn't need to save against the tremors.

**Heightened (9th)** The wave explodes on one additional target of your choice in the line to the final target.

**Source:** `= this.source` (`= this.source-type`)
