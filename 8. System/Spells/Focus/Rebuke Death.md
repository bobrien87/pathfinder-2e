---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Focus]]", "[[Healing]]", "[[Manipulate]]", "[[Vitality]]"]
cast: "1 to 3"
area: "20-foot emanation"
targets: "1 living creature per action spent to Cast this Spell"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You snatch creatures from the jaws of death, restoring them without the straing of a typical close call. You can spend 1 to 3 actions Casting this Spell, and you can target a number of creatures equal to the actions spent. Each target regains 3d6 Hit Points. If the target had the [[Dying]] condition, coming back from Dying due to this healing doesn't increase its [[Wounded]] condition.

**Heightened (+1)** Increase the healing by 1d6.

**Source:** `= this.source` (`= this.source-type`)
