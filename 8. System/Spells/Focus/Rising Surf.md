---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Focus]]", "[[Manipulate]]", "[[Move]]", "[[Water]]"]
cast: "`pf2:1`"
range: "30 feet"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a wave of water that you ride, banking around obstacles and surfing to higher ground. You move up to 35 feet, raising yourself up to 5 feet above the ground. (You can avoid many types of difficult terrain in this way.) You must end your movement on an unoccupied space where you have solid footing. This movement isn't a Stride, but you measure the distance in a similar way, and it still triggers reactions caused by movement. You can't transport anyone else with you.

**Heightened (+2)** Increase the distance you move by 5 feet and the maximum height traveled above the ground by 5 feet.

**Source:** `= this.source` (`= this.source-type`)
