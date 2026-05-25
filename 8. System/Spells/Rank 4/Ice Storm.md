---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "20-foot burst"
defense: "basic Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a gray storm cloud that pelts creatures with an icy deluge. When you Cast the Spell, a burst of magical hail deals 2d8 bludgeoning damage and 2d8 cold damage to each creature in the area below the cloud (basic Reflex save). Snow and sleet continue to rain down in the area for the remainder of the spell's duration, making the area difficult terrain. Any creature that ends its turn in the storm takes @Damage[(floor(@item.level/2))[cold]] damage. If you Cast this Spell outdoors, you can create two nonoverlapping clouds instead of one. As normal, if a Large or larger creature is in both clouds, it still only takes the initial damage once and the continuing damage once per turn.

**Heightened (+2)** The initial bludgeoning damage and cold damage increase by 1d8 each, and the cold damage creatures take at the end of their turns increases by 1.

**Source:** `= this.source` (`= this.source-type`)
