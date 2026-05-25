---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Focus]]", "[[Illusion]]", "[[Manipulate]]", "[[Mental]]", "[[Ranger]]"]
cast: "`pf2:2`"
area: "10-foot emanation"
defense: "Will"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You appear larger and stronger to nearby creatures, appearing to possess threatening features like antlers, claws, or poison to their senses. Each non-allied creature in the area must attempt a Will save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1. This condition doesn't decrease at the end of its turn if it damaged you during that turn.
- **Failure** As success, but [[Frightened]] 2.
- **Critical Failure** As success, but [[Frightened]] 3.

**Source:** `= this.source` (`= this.source-type`)
