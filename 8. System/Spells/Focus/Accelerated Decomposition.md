---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Oracle]]", "[[Void]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Fortitude"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You speed the natural process of a creature's decline and debilitation. As its body withers, the target takes 9d6 void damage and must attempt a Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage and is your choice of [[Clumsy]] 1, [[Drained]] 1, or [[Enfeebled]] 1 for 1 round.
- **Failure** The target takes full damage and is clumsy 1, drained 1, and enfeebled 1 for 1 round.
- **Critical Failure** The creature takes double damage and is clumsy 1, drained 1, and enfeebled 1 for 1 minute.

**Heightened (+1)** The void damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
