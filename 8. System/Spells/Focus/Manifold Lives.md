---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]", "[[Oracle]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 target"
defense: "Will"
duration: "varies"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cast a creature's mind back through time, forcing them to take other paths and make other choices, experiencing countless alternate lives in an instant. The creature becomes overwhelmed with regret over paths untraveled, lives unlived, and times unrealized. The creature takes 6d6 mental damage and must attempt a Will save. After the effect is resolved, the target is then temporarily immune for 1 day.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Stupefied 2]] for 1 round.
- **Failure** The creature takes full damage and is stupefied 2 for 1 minute. While affected, the creature must attempt another save at the start of its turn; on a failure, it's [[Slowed]] 1 for that turn as it sobs uncontrollably.
- **Critical Failure** The creature takes double damage and for 1 minute, it's [[Stupefied 4]] and slowed 1 as it sobs uncontrollably.

**Heightened (+1)** The mental damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
