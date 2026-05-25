---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "30 feet"
targets: "up to 10 creatures, including yourself"
defense: "basic Fortitude"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The Ten Magic Warriors were the first of the Magaambya's students, and they come to your aid even now. An indistinct spirit appears near each target, each wearing a different mask of the Ten Magic Warriors. The spirits then either strike their designated targets with magical energy, dealing each one 4d6 spirit damage with a basic Fortitude save, or shield them, granting their target resistance 3 to physical and spirit damage until the beginning of your next turn. You designate which targets are attacked and which are shielded.

> [!danger] Effect: Spell Effect: Call the Ten

**Heightened (+2)** The amount of damage increases by 1d6 and the amount of resistance increases by 2.

**Source:** `= this.source` (`= this.source-type`)
