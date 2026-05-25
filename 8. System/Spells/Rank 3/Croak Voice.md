---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]", "[[Morph]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause the target creature's vocal chords to swell like those of a frog. The target must attempt a Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target's voice becomes hoarse, and speaking becomes painful. Whenever it uses an action that has the auditory trait or attempts to Cast a Spell that doesn't have the subtle trait, it must succeed at a DC 5 flat check or the action is lost. Once per round, the target can spend an Interact action to massage its throat, attempting a Fortitude save against your spell DC. On a success, the spell ends.
- **Failure** As success, but using an action with the auditory trait also deals 2d10 mental damage to the target as the sound of its distorted voice grates on its ears.
- **Critical Failure** As failure, but the damage for using an action with the auditory trait is doubled, and the target can't use an Interact action to attempt a Fortitude save to end the effect early.

**Heightened (+1)** The damage for using an action with the auditory trait increases by 1d10.

**Source:** `= this.source` (`= this.source-type`)
