---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]", "[[Subtle]]"]
cast: "`pf2:r`"
duration: "1 minute"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You're exposed to a poison or disease that has the inhaled trait, and you're aware of the exposure

**Requirements** You breathe air.

You suck in a rough breath of air, and your body automatically filters out the harmful molecules that would infest your lungs. As you breathe for the duration of the spell, you get the outcome one degree of success higher on your saving throws against inhaled poisons and diseases.

> [!danger] Effect: Spell Effect: Filter Air

**Source:** `= this.source` (`= this.source-type`)
