---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Oracle]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You share some of your own temporal distortions with a foe, altering their mind and body unpredictably as they're thrown backward or forward in time. Roll `r 1d4`. On a 1, the foe becomes clumsy; on a 2, it becomes enfeebled; on a 3, it becomes stupefied; and on a 4, you choose which condition applies.
- **Critical Success** The target is unaffected.
- **Success** The target is either [[Clumsy]] 1, [[Enfeebled]] 1, or [[Stupefied 1]] for 1 round, depending on the result of the d4.
- **Failure** The target is either clumsy 1, enfeebled 1, or stupefied 1 for 4 rounds, depending on the result of the d4.
- **Critical Failure** As failure, but the time warp is stronger, increasing the condition's effects but making it run its course faster. The condition's value is 3, and the condition lasts for 2 rounds.

**Source:** `= this.source` (`= this.source-type`)
