---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Illusion]]", "[[Manipulate]]", "[[Subtle]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 willing creature"
duration: "10 minutes (sustained)"
source: "Pathfinder NPC Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The only thing thieves love more than being silent and stealthy is the piles of gold they win with that silence and stealth. You mask the target with multiple illusions combined in a perfect mix, affecting them with both the [[Invisibility]] and [[Silence]] spells. If the target takes a hostile action, *burglar's blind* and both the spells it grants end after the hostile action is completed.

**Heightened (5th)** You can target up to 5 willing creatures. The spells end for all targets if any one of them takes a hostile action.

**Source:** `= this.source` (`= this.source-type`)
