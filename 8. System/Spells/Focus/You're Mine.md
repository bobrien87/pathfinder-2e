---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Focus]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]", "[[Sorcerer]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 round"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You manipulate the target's emotions, potentially allowing you to control it for a brief instant. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Stunned]] 1.
- **Failure** On the target's next turn, it's [[Stunned]] 1 and you partially control it, causing it to take a single action of your choice. If it has actions left, it can act normally.
- **Critical Failure** The target is [[Controlled]] for 1 round.

**Heightened (7th)** On a failure, the target is Controlled for 1 round. On a critical failure, the target is Controlled for up to 1 minute; it receives a new Will save at the end of each of its turns, and on a success, the spell ends.

**Source:** `= this.source` (`= this.source-type`)
