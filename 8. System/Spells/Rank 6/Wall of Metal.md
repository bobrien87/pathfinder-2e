---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:3`"
range: "120 feet"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call forth a sheet of metal, forming a wall of iron, low-grade cold iron, or standard-grade silver up to 60 feet long, 30 feet high, and 1/4 inch thick. The wall doesn't need to stand vertically but must form a straight line in an unbroken open space so it doesn't pass through any creatures or objects, or the spell is lost. Each 10-foot-by-10- foot section of the wall has AC 10 and is immune to critical hits and precision damage. The wall's Hardness, HP, and BT use the statistics of a structure of the material you chose. Creatures can move through a section of the wall that's broken.

**Heightened (7th)** The wall is high-grade silver or standard-grade dawnsilver.

**Heightened (8th)** The wall is standard-grade cold iron.

**Heightened (9th)** The wall is high-grade dawnsilver.

**Heightened (10th)** The wall is high-grade cold iron or standard-grade adamantine.

**Source:** `= this.source` (`= this.source-type`)
