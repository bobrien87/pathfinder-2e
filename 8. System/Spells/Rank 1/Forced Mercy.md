---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You soften the target's blows, ensuring they avoid vital areas and cause no lasting harm. All physical damage dealt by the target to living creatures becomes nonlethal and all persistent bleed damage dealt by the target is reduced to 0. This effect doesn't incur the typical –2 circumstance penalty for nonlethal attacks with a lethal weapon or attack. An unwilling target must attempt a Will save. A willing target can choose to critically fail their saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature is affected for 1 round.
- **Failure** The creature is affected for 1d4 rounds.
- **Critical Failure** The creature is affected for 1 minute.

**Heightened (4th)** The range increases to 100 feet, and you can target up to 8 creatures.

**Source:** `= this.source` (`= this.source-type`)
