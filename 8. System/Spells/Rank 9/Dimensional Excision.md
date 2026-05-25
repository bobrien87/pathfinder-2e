---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
defense: "basic Will"
source: "Pathfinder #212: A Voice in the Blight"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You manipulate the boundaries between planes like a scalpel, using it to cut away portions of a creature's essence and banishing those portions to other realities and dimensions, afflicting the target deep lacerations or even severed appendages. The creature takes 14d10 damage (no damage type) and 2d10 persistent bleed damage and must attempt a Will save. If the target is not on its home plane, it takes a –4 status penalty to this save. A creature reduced to 0 HP has their entire body sectioned out and banished across multiple planes and dimensions, leaving nothing behind but their gear.

**Heightened (10th)** The base damage increases by 2d10, and the persistent bleed damage by 1d10.

**Source:** `= this.source` (`= this.source-type`)
