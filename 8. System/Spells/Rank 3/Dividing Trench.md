---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
duration: "1 minute"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You dig an earthen trench across the surrounding terrain, which must be soil, clay, sand, or other soft earth, but not flooring or stone. The trench is 5 feet wide, 5 feet deep, and up to 15 feet long. You can shape the trench's path, but it must be one continuous line. You must conjure the trench in an open space so it doesn't pass through any creatures or objects. Creatures inside the trench have cover from creatures outside the trench, and creatures outside the trench have cover from creatures inside the trench. Small or smaller creatures in the trench might have greater cover against other creatures who aren't close to the trench's edge, and in turn, those creatures might have more cover against small creatures in the trench; the GM determines the amount of additional cover, if any. Entering or leaving the trench requires an additional 5 feet of movement but doesn't require any kind of check and isn't considered difficult terrain. At the end of the spell's duration, the trench disappears, and all creatures in the trench remain in their spaces on solid ground.

**Heightened (+2)** The trench's maximum length increases by 15 feet.

**Source:** `= this.source` (`= this.source-type`)
