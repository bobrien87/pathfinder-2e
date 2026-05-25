---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Fire]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You send a bubble of viscous liquid that sparks into flame. Make a spell attack roll against the target's AC, dealing 1d8 fire damage and 1d8 persistent fire damage on a hit. The target is [[Enfeebled]] 1 until they recover from their persistent fire damage.

**Heightened (+2)** The initial and persistent fire damage increase by 1d8.

**Source:** `= this.source` (`= this.source-type`)
