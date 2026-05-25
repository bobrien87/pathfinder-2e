---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
cast: "1 hour"
duration: "up to 10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You tear the veil to the afterlife and call a spirit from its final resting place. You must call the spirit by name, and you must provide a connection to the spirit, such as a possession, a garment, or a piece of its corpse. A spirit unwilling to heed your call can attempt a Will save to avoid it; on a critical success, a trickster spirit Impersonates the spirit you meant to call. The DC of the Will save is 2 lower if you haven't met the spirit in life. Either way, the spirit appears as a wispy form of the creature you meant to call. Each minute of the duration, you can ask the spirit a question. It can answer how it pleases or even refuse to answer. If the spirit isn't in the afterlife (such as if it's an undead), all results other than critical failures use the failure effect.
- **Critical Success** The spirit is particularly cooperative, and even if it has strong reasons to deceive you, it takes a -2 circumstance penalty to its Deception checks.
- **Success** You call the spirit.
- **Failure** You fail to call a spirit.
- **Critical Failure** One or more evil spirits appear and attack.

**Source:** `= this.source` (`= this.source-type`)
