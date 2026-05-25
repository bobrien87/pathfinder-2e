---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Illusion]]", "[[Manipulate]]", "[[Subtle]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 willing creature"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The target makes no sound, preventing creatures from noticing it using hearing alone. The target can't use sonic attacks, nor can it use actions with the auditory trait. This prevents it from casting spells due to the magical words involved in casting, with the exception of subtle spells.

> [!danger] Effect: Spell Effect: Silence

**Heightened (4th)** The spell creates an aura in a 10-foot emanation around the touched creature, silencing all sound in or passing through it. While within the aura, creatures are subject to the same effects as the target. Depending upon the position of the effect, a creature might notice the lack of sound reaching it (blocking off the noise coming from a party, for example).

**Source:** `= this.source` (`= this.source-type`)
