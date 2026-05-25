---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Mental]]"]
cast: "`pf2:r`"
range: "30 feet"
targets: "the triggering foe"
defense: "Will"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You critically fail a saving throw against a foe's effect.

You distract your enemy with their feeling of smug pleasure when you fail catastrophically. They must attempt a Will save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is distracted by its amusement and takes a -1 status penalty on Perception checks and Will saves for 1 round. 

> [!danger] Effect: Spell Effect: Schadenfreude (Success)
- **Failure** The creature is overcome by its amusement and is [[Stupefied 1]] for 1 round.
- **Critical Failure** The creature is lost in its amusement and is [[Stupefied 2]] for 1 round and [[Stunned]] 1.

**Source:** `= this.source` (`= this.source-type`)
