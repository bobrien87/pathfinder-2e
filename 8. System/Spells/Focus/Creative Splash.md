---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Illusion]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "5-foot burst"
defense: "Will"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A deluge of paint or colorful illusions descend on the area, reflecting your personal creative specialty. Roll `r 1d4 #Creative Splash` to determine the color of the illusion. Each creature in the area must succeed at a Will save or take the effect listed on the table for the color.

1d4ColorFailureCritical Failure1White[[Dazzled]] for 1 roundDazzled for 1 minute2Red[[Enfeebled]] 1 for 1 round[[Enfeebled]] 2 for 1 round3Yellow[[Frightened]] 1[[Frightened]] 24Blue[[Clumsy]] 1 for 1 round[[Clumsy]] 2 for 1 round

**Source:** `= this.source` (`= this.source-type`)
