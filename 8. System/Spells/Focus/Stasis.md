---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Incapacitation]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature or up to 1 Bulk of objects"
defense: "Will"
duration: "varies"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The flow of time congeals around an object or creature, holding it in place. The target must attempt a Will save (an unattended object automatically critically fails its save).
- **Critical Success** The target is unaffected.
- **Success** The target is [[Stunned]] 1 as time thickens around it.
- **Failure** Time ceases to pass for the target for 1 round. It is invulnerable to all damage, it can't be targeted or affected by anything, and no rounds elapse for any timed durations, conditions, afflictions, and other effects it has. While in stasis, the target can't be moved, and it remains fixed in place, defying gravity if need be.
- **Critical Failure** As failure, but the target is held in stasis for 3 rounds. At the end of each of its turns, it can attempt a Will save to reduce the remaining duration by 1 round or end it entirely on a critical success.

**Source:** `= this.source` (`= this.source-type`)
