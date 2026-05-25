---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Fire]]", "[[Holy]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You shine a blazing ray of light tinged with holy energy. Make a ranged spell attack. The ray deals 5d6 fire damage. If the target has the unholy trait, you deal an extra 5d6 spirit damage.
- **Critical Success** The target takes double damage.
- **Success** The target takes full damage.

If the light passes through an area of magical darkness or targets a creature affected by magical darkness, *holy light* attempts to counteract the darkness. If you need to determine whether the light passes through an area of darkness, draw a line between yourself and the spell's target.

**Heightened (+1)** The fire damage increases by 2d6, and the spirit damage against unholy creatures increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
