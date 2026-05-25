---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Disease]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
defense: "Fortitude"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your touch afflicts the target with an advanced form of scurvy, a mariner's disease stemming from improper nutrition. The symptoms of scurvy include fatigue, joint pain, loose teeth, and internal hemorrhaging.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Enfeebled]] 1 for 1 minute.
- **Failure** The target is afflicted with advanced scurvy at stage 1.
- **Critical Failure** The target is afflicted with advanced scurvy at stage 2.

**Advanced Scurvy** (disease)

**Level** 4

for 1 day after eating fresh fruit, a creature gains a +2 circumstance bonus to their next saving throw against this affliction

**Stage 1** enfeebled 1 and the damage dealt by persistent bleed effects is increased by 1 (1 day)

**Stage 2** enfeebled 1, [[Fatigued]], and the damage dealt by persistent bleed effects is increased by 1d4 (2 days)

**Stage 3** [[Enfeebled]] 2, fatigued, and the damage dealt by persistent bleed effects is increased by 1d6 (4 days)

**Source:** `= this.source` (`= this.source-type`)
