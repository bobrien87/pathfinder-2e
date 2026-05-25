---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Emotion]]", "[[Focus]]", "[[Mental]]", "[[Subtle]]"]
cast: "`pf2:r`"
range: "60 feet"
targets: "one creature being influenced"
defense: "Will"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You or an ally in range attempt to use a mental effect to convince a creature to do something (such as a [[Coerce]], [[Request]], or a [[Suggestion]] spell).

You strengthen a target's ambition, increase its resentment of allies, and make its allegiances more susceptible to change. The target must attempt a Will save.
- **Critical Success** The target is unaffected and realized you attempted to influence its reaction with magic.
- **Success** The target takes a -1 status penalty to its defenses against the triggering effect. This penalty is -2 if the target is being encouraged to advance its own ambitions.The target doesn't realize you Cast the Spell on it.
- **Failure** As success, but the penalty is -4 if the target is being encouraged to advance its own ambitions.
- **Critical Failure** As success, but the creature automatically follows a suggestion that advances its own ambitions.

**Source:** `= this.source` (`= this.source-type`)
