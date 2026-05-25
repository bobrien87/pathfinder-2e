---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Emotion]]", "[[Focus]]", "[[Mental]]", "[[Misfortune]]"]
cast: "`pf2:r`"
range: "30 feet"
targets: "An enemy that critically failed an attack roll, Perception check, or skill check"
defense: "Will"
duration: "varies"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** An enemy within 30 feet of you critically fails an attack roll, Perception check, or skill check.

You mock the target for all its failings, twisting its self-confidence into doubt. The enemy attempts a Will saving throw.
- **Success** The target is unaffected.
- **Failure** The target is briefly shaken and unsure of its abilities. It must roll twice and take the worse result on the next roll of the same type as the critical failure that triggered the spell (such as the target's next Acrobatics check if the spell's trigger was a critical failure on an Acrobatics check). If the target doesn't attempt any qualifying checks, the spell ends at the end of the target's next turn.

**Source:** `= this.source` (`= this.source-type`)
