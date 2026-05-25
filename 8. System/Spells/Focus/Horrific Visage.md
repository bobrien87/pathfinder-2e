---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Focus]]", "[[Illusion]]", "[[Manipulate]]", "[[Mental]]", "[[Sorcerer]]", "[[Visual]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
defense: "Will"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You briefly transform your features into the horrific visage of a hag, striking fear into your enemies. Foes in the area must attempt a Will save.
- **Success** The foe is unaffected.
- **Failure** The foe is [[Frightened]] 1.
- **Critical Failure** The foe is [[Frightened]] 2.

**Heightened (5th)** Foes in the area are [[Frightened]] 1 on a success, [[Frightened]] 2 on a failure, and [[Frightened]] 3 and [[Fleeing]] for 1 round on a critical failure. They are still unaffected on a critical success.

**Source:** `= this.source` (`= this.source-type`)
