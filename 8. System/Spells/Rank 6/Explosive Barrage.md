---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]", "[[Sonic]]"]
cast: "`pf2:2`"
range: "100 feet"
area: "20-foot burst"
defense: "basic Fortitude"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** (continued) 20-foot burst plus additional @Template[burst|distance:5]{5-foot bursts}

You fire a booming, fiery explosion followed by a salvo of smaller blasts, each cracking the air with the sound of thunder. You create a 20-foot burst and `r 1d4#Additional 5-foot bursts` additional 5-foot bursts each within the range and within 20 feet of another burst. None of the bursts can intersect. Each creature caught in at least one of these bursts takes 6d8 fire damage and 6d4 sonic damage (basic Fortitude save). On a failed save, a creature is also [[Deafened]] for 1 minute.

**Heightened (+1)** The fire damage increases by 1d8 and the sonic damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
