---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Death]]", "[[Manipulate]]", "[[Void]]"]
cast: "`pf2:2`"
area: "40-foot emanation"
defense: "Fortitude"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You howl a lament of damned souls. Each living enemy in the area takes 8d10 void damage and must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes full damage.
- **Failure** The creature takes full damage and is [[Drained]] `r 1d4`.
- **Critical Failure** The creature takes double damage and is [[Drained]] 4.

**Source:** `= this.source` (`= this.source-type`)
