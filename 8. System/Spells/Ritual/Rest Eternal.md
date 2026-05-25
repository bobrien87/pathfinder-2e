---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
cast: "1 day"
range: "20 feet"
targets: "1 dead creature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon gods, spirits, and stranger beings to bar a creature's spirit from ever returning. A spirit that doesn't wish to be so constrained can attempt a Will save to resist this ritual; on a critical success, it fools you into believing the ritual succeeded. This ritual has no effect on a target who is undead or whose soul is otherwise not in the afterlife.
- **Critical Success** You sequester the subject's spirit to the afterlife. Attempts to communicate with the dead creature, return it to life, turn it into an undead, or otherwise disturb its afterlife fail unless the effect's counteract rank is at least 2 higher than that of rest eternal or originates from an artifact or a deity. Successfully returning the creature to life ends the restrictions placed by rest eternal.
- **Success** As critical success, but effects to interact with the spirit fail unless the effect's counteract rank is higher than that of rest eternal or originates from an artifact or a deity.
- **Failure** The ritual has no effect.
- **Critical Failure** The ritual fails, and the spirits you appealed to are angered. All casters become [[Doomed]] 1 for 1 week.

**Source:** `= this.source` (`= this.source-type`)
