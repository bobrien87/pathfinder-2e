---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Incapacitation]]", "[[Linguistic]]", "[[Manipulate]]", "[[Mental]]", "[[Subtle]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You implant a subconscious suggestion deep within the target's mind for them to follow when a trigger you specify occurs. You suggest a course of action to the target. Your directive must be phrased in such a way as to seem like a logical course of action to the target, and it can't be self-destructive or obviously against the target's self-interest. The target must attempt a Will save.
- **Critical Success** The target is unaffected and knows you tried to control it.
- **Success** The target is unaffected and thinks you were talking to them normally, not casting a spell on them.
- **Failure** The suggestion remains in the target's subconscious until the next time you prepare. If the trigger occurs before then, the target immediately follows your suggestion. The effect has a duration of 1 minute, or until the target has completed a finite suggestion or the suggestion becomes self-destructive or has other obvious negative effects.
- **Critical Failure** As failure, but the duration is 1 hour.

**Heightened (9th)** You can target up to 10 creatures.

**Source:** `= this.source` (`= this.source-type`)
