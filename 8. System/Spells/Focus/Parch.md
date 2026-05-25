---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Air]]", "[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
defense: "basic Fortitude"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Dry winds dehydrate a creature. The target must attempt a Fortitude save; if used on a creature that has the water trait or a creature made primarily of liquid (such as many oozes), the creature uses the outcome for one degree of success worse than the result. Creatures whose bodies contain no significant moisture (such as earth elementals) are immune to parch.

If a creature affected by parch drinks a liquid, such as a swig of water or a potion, the spell ends. Affected creatures that have the water trait or are made primarily of liquid, as well as affected creatures that can't drink, can end the effect as a two-action activity, which has the concentrate trait.
- **Critical Success** The target is unaffected.
- **Success** The target takes a –1 status penalty to its checks and DCs for 1 round.
- **Failure** The target takes a –1 status penalty to its checks and DCs for 1 minute.
- **Critical Failure** The target takes a –2 status penalty to its checks and DCs for 1 minute and is [[Dazzled]] as long as it has this penalty.

**Heightened (4th)** You can target up to 4 creatures.

**Source:** `= this.source` (`= this.source-type`)
