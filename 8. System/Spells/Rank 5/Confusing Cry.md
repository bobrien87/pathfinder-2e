---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "20-foot emanation"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You give an unsettling, warbling cry that causes nearby creatures to lash out without control. Each creature in the area that can hear must attempt a Will save.
- **Critical Success** The target is unaffected and immune to this spell for 1 minute.
- **Success** The target is [[Stunned]] 1.
- **Failure** The target is [[Confused]] for 1 minute. It can attempt a new save at the end of each of its turns to end the confusion.
- **Critical Failure** As failure, and the creature immediately attacks itself. This Strike doesn't give the creature a flat check to recover from the confusion.

**Source:** `= this.source` (`= this.source-type`)
