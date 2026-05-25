---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cloud the target's mind with vivid, dreamlike imagery, so they have difficulty distinguishing real threats from imagined ones.
- **Critical Success** The target is unaffected.
- **Success** The target is distracted by the visions and treats all other creatures as [[Concealed]] for 1 round, and you can't Sustain the Spell to increase the duration.
- **Failure** The target is [[Confused]]. In addition to the creatures present, the target might also attack wildly at thin air, attempting to fend off the dreams. It can attempt a new save at the end of each of its turns to end the confusion. Even if the confused effect ends early, the target treats all other creatures as concealed for 1 round.
- **Critical Failure** As failure, but the target gets no save to end the effect early.

**Source:** `= this.source` (`= this.source-type`)
