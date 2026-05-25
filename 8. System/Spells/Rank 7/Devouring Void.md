---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Void]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "30-foot burst"
defense: "basic Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Countless tears in space appear in the area, like hungry mouths. When the spell is cast and the first time each round it's sustained, living creatures in its area take 7d8 void damage (basic Fortitude save). A living creature using a move action to leave the area must succeed at a [[Reflex]] save or their action is disrupted at the edge of the area.

**Heightened (+1)** The void damage increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
