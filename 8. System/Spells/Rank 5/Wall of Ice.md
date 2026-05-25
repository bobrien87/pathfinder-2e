---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:3`"
range: "120 feet"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You sculpt an ice barrier that blocks sight and, once shattered, freezes foes. You create either a 1-foot-thick wall of ice in a straight line up to 60 feet long and 10 feet high (the wall doesn't have to be vertical, but it must be anchored on both sides to a solid surface) or a 1-foot-thick, 10-foot radius hemisphere of ice. The ice that makes up the wall is opaque. If you wish, the wall can be of a smaller length, height, or radius.

You must create the wall in an unbroken open space so its edges don't pass through any creatures or objects, or the spell is lost. Each 10-foot-by-10-foot section of the wall has AC 10, Hardness 10, and 40 Hit Points, and it's immune to critical hits, cold damage, and precision damage. A section also has weakness 15 to fire; a section of the wall destroyed by fire melts, evaporating into water and steam. A section destroyed by means other than fire leaves behind a chilling mass of ice that is difficult terrain and deals 2d6 cold damage to any creature passing through it.

**Heightened (+2)** The Hit Points of each section of the wall increase by 10, and the cold damage dealt to creatures crossing a destroyed section increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
