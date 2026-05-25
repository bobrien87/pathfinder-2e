---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Lotuses, water lilies, and other watery plants bloom at your feet, allowing you to walk on the surface of water and other liquids. You can go underwater if you wish, but in that case, you must Swim normally. As you Stride or Step on water, you leave a trail of oversized lily pads, lotus leaves, or spatterdock that fill the squares' surfaces in your wake. Each square of this trail can withstand the weight of 1 Medium creature and lasts until the end of your next turn. You can Dismiss this spell early.

**Heightened (4th)** The duration of this spell increases to 10 minutes. The trail lasts until the spell ends or you Dismiss the spell on you, whichever comes first.

**Heightened (6th)** The duration increases to 1 hour. Your trail is permanent even if you Dismiss the spell on you, although if the water can't support such plants, they'll die in a week. The trail can be removed by dispel magic or a similar spell.

**Source:** `= this.source` (`= this.source-type`)
