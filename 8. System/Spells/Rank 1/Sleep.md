---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]", "[[Sleep]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "5-foot burst"
defense: "Will"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Each creature in the area becomes drowsy, possibly nodding off. A creature that falls [[Unconscious]] from this spell doesn't fall [[Prone]] or release what it's holding. This spell doesn't prevent creatures from waking up due to a successful Perception check, limiting its utility in combat.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes a –1 status penalty to Perception checks for 1 round.
- **Failure** The creature falls unconscious. If it's still unconscious after 1 minute, it wakes up automatically.
- **Critical Failure** The creature falls unconscious. If it's still unconscious after 1 hour, it wakes up automatically.

**Heightened (4th)** The creatures fall unconscious for 1 round on a failure or 1 minute on a critical failure. They fall prone and release what they're holding, and they can't attempt Perception checks to wake up. When the duration ends, the creature is sleeping normally instead of automatically waking up.

**Source:** `= this.source` (`= this.source-type`)
