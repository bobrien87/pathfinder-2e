---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "up to 5 creatures"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Fleeting notes of a strange and unnatural song fill the air, overtaking the mind. Each target must attempt a Will save when you cast the spell, and again the first time you Sustain this Spell each round. A creature needs to attempt only one save against the song each round, and you have to keep the same targets when you Sustain the Spell.
- **Critical Success** The target is unaffected, can't be affected on subsequent rounds, and is temporarily immune for 1 minute.
- **Success** The target is unaffected this round, but it can be affected on subsequent rounds.
- **Failure** Roll `r 1d4` on the table below.
- **Critical Failure** Roll `r 1d4+1` on the table below.

ResultEffect1The target is [[Frightened]] 22The target is [[Confused]] for 1 round3The target is [[Stupefied 4]] for 1 round4The target is [[Blinded]] for 1 round5The target is [[Stunned]] for 1 round and [[Stupefied 1]] for an unlimited duration

**Source:** `= this.source` (`= this.source-type`)
