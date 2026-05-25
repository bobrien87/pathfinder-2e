---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Cantrip]]", "[[Cold]]", "[[Concentrate]]", "[[Fire]]", "[[Manipulate]]", "[[Psychic]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "5-foot square"
defense: "basic Fortitude"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** two adjacent 5-foot squares

Energy attempts to balance out, but with your magic, you can shunt all the energy in one area to another. Creatures in either area take 4d4 damage with a basic Fortitude save. Choose one of the squares to steal heat, dealing cold damage, and the other to concentrate the stolen heat, dealing fire damage. A creature that fails its save also becomes [[Clumsy]] 1 from numbness if it's in the area of stolen heat or [[Enfeebled]] 1 from heat stroke if it's in the area of concentrated heat; these conditions last until the start of your next turn. If a creature is large enough to be in both squares, you choose only one of the areas for it to attempt its save against; it's unaffected by the other area.

**Heightened (+1)** The damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
