---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Linguistic]]", "[[Manipulate]]", "[[Mental]]"]
cast: "1 minute"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cast your thoughts through a creature's mind, sifting for information. You access the target's memories and knowledge unless it fends you off with a Will save.
- **Success** The target is unaffected.
- **Failure** Each round of the spell's duration, you can Sustain the spell to ask a different question and attempt to uncover the answer. For each question, the target can attempt a Deception check against your spell DC; if the target succeeds, you don't learn the answer, and on a critical success, the target gives you a false answer that you believe is truthful Once you've asked the target a given question, asking it again, even with a separate casting of mind probe, produces the same result.
- **Critical Failure** As failure, and the target takes a –4 circumstance penalty to Deception checks against your questions.

**Source:** `= this.source` (`= this.source-type`)
