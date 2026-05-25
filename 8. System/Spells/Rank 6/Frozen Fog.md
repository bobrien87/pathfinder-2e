---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "20-foot burst"
defense: "basic Fortitude"
duration: "1 minute"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a chilling mist that settles into the bones and makes it difficult to move. This has the effects of [[Mist]], except that you can Sustain the spell once per round to move the fog up to 10 feet. A creature that starts its turn in the area takes 6d8 cold damage with a basic Fortitude save. A creature that fails its save is also [[Clumsy]] 1 for 1 minute ([[Clumsy]] 2 on a critical failure) and takes a –10-foot status penalty to Speeds for as long as it's clumsy.

> [!danger] Effect: Spell Effect: Frozen Fog

**Heightened (+2)** The damage increases by 3d8.

**Source:** `= this.source` (`= this.source-type`)
