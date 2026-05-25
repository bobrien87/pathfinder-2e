---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Attack]]", "[[Cold]]", "[[Concentrate]]", "[[Darkness]]", "[[Manipulate]]", "[[Unholy]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You shoot an utterly cold ray of darkness tinged with unholy energy. Make a ranged spell attack. The ray deals 5d6 cold damage. If the target has the holy trait, you deal an extra 5d6 spirit damage.
- **Critical Success** The target takes double damage.
- **Success** The target takes full damage.

If the ray passes through an area of magical light or targets a creature affected by magical light, *chilling darkness* attempts to counteract the light. If you need to determine whether the ray passes through an area of light, draw a line between yourself and the spell's target.

**Heightened (+1)** The cold damage increases by 2d6, and the spirit damage against holy creatures increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
