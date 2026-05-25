---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Cleric]]", "[[Concentrate]]", "[[Fire]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
duration: "until the end of the target's next turn"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A blazing band of fire arcs through the air, lighting your opponent and the ground they stand upon on fire. Make a spell attack roll against the target's AC. The ray deals 2d6 fire damage on a hit (or double damage on a critical hit). On any result other than a critical failure, the ground in the target's space catches fire, dealing @Damage[(@item.rank)d6[fire]] damage to each creature that ends its turn in one of the squares.

**Heightened (+1)** The ray's initial damage increases by 2d6, and the fire damage dealt by the burning space increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
