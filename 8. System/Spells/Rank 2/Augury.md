---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Prediction]]"]
cast: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You gain a vague glimpse of the future. During the casting of this spell, ask about the results of a particular course of action. The spell can predict results up to 30 minutes into the future and reveal the GM's best guess among the following outcomes: good, bad, mixed (the results will be a mix of good and bad), and nothing (there won't be particularly good or bad results).

The GM rolls a secret DC 6 flat check. On a failure, the result is always "nothing." This makes it impossible to tell whether a "nothing" result is accurate. If anyone asks about the same topic as the first casting of *augury* during an additional casting, the GM uses the secret roll result from the first casting. If circumstances change, though, it's possible to get a different result.

**Source:** `= this.source` (`= this.source-type`)
