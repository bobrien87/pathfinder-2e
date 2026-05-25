---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
duration: "until the next time you make your daily preparations"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Powerful wards hide a creature from magic that would spy on it or affect its mind. The target gains a +4 status bonus to saves against mental effects. *Hidden mind* attempts to counteract any detection, revelation, and scrying effects as if its spell rank were 1 higher than its actual rank. On a success, the effect functions normally except that it detects nothing about the target and its possessions. For instance, *detect magic* would still detect other magic in the area, but not any magic on the target.

> [!danger] Effect: Spell Effect: Hidden Mind

**Source:** `= this.source` (`= this.source-type`)
