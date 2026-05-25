---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Air]]", "[[Concentrate]]", "[[Healing]]", "[[Manipulate]]", "[[Vitality]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "40-foot burst"
duration: "10 Minutes"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A light, soothing breeze flows through the area, making it easier to rest and recover. Medicine checks attempted to benefit living creatures in the area get a +2 status bonus. Any living creature in the area also gets a +2 status bonus to saving throws against afflictions and, if it remains within the area for the full duration, regains 10 Hit Points. In addition, the cool breeze reduces the temperature effects of heat by one step for any creature in the area.

**Heightened (+2)** The healing increases by 10 Hit Points.

**Source:** `= this.source` (`= this.source-type`)
