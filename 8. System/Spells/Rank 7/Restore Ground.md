---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "30-foot burst"
duration: "varies"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You sense that this place yearns to throw off the shackles of civilization. You attempt to restore the area within the burst to a natural state, removing all artificial objects and buildings and encouraging the growth of plants on the ground that remains. Creatures are unaffected unless caught in a structural collapse.

- **Ground** All ground within the area becomes greater difficult terrain for 1 round.
- **Objects** Any unattended object of Bulk 4 or less is destroyed, regardless of Hardness, unless it's an artifact or similarly hard to destroy.
- **Plants** Plants in the area become healthier and more fruitful for 1 year.
- **Structures** Structures within range are shaken and may collapse, as if affected by [[Earthquake]].

**Source:** `= this.source` (`= this.source-type`)
