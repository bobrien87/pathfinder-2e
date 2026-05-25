---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature that isn't on its home plane"
defense: "Will"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You send the target back to its home plane. The target must attempt a Will save. You can spend an extra action while Casting this Spell and add a cost to the spell to give the creature a –2 circumstance penalty to its save. The cost must be a specially gathered object that is anathema to the creature. This spell fails if you aren't on your home plane when you cast it.
- **Critical Success** The target resists being banished and you are [[Stunned]] 1.
- **Success** The target resists being banished.
- **Failure** The target is banished.
- **Critical Failure** The target is banished and can't return by any means to the plane it's banished from for 1 week.

**Heightened (9th)** You can target up to 10 creatures. The extra cost affects targets to which it is anathema.

**Source:** `= this.source` (`= this.source-type`)
