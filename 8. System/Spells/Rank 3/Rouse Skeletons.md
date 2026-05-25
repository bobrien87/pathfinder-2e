---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "10-foot burst"
defense: "basic Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Misshapen skeletal forms erupt from a solid surface, such as a stone floor, and fill the burst. The area they fill is difficult terrain. Their grasping claws deal 2d6 slashing damage to creatures on the ground in the area when the skeletons first appear with a basic Reflex save.

On subsequent rounds, the first time you Sustain the Spell each round, you can move the area of skeletons up to 20 feet within the range of the spell and deal 2d6 slashing damage with a basic Reflex save to each creature in the new area.

Damaging or destroying the skeletons is irrelevant, as new bones pull forth from the ground to repair and replace any that are obliterated.

**Heightened (+2)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
