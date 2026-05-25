---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "60-foot line"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You even out the ground and push aside low obstacles. Non-magical difficult terrain or greater difficult terrain composed of earth, rubble, sand, and the like in the area becomes normal terrain. You can attempt a counteract check against magical difficult terrain and greater difficult terrain composed of earthen materials in the area, too, making it normal terrain for the duration if you succeed. The ground doesn't change quickly enough to cause anyone to lose footing, and it doesn't clear concealing features enough to make them non-concealing. At the GM's discretion, if you use this spell on "ground" that has no underlying surface to flatten and clear, such as ice on the surface of a lake, the spell fails.

**Heightened (4th)** The area increases to a @Template[line|distance:120] along the ground.

**Heightened (6th)** The area increases to a @Template[line|distance:500] along the ground.

**Source:** `= this.source` (`= this.source-type`)
