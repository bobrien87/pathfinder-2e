---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "30 feet"
area: "5-foot square"
targets: "one unoccupied 5-foot square"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You summon a swarm of bees from the city of Axis that rapidly constructs geometric shapes from wax. The bees appear in an unoccupied square, building a structure of hexagons, squares, and decagons that fill the space. The wax shape has a Hardness of 10 and 40 Hit Points but also decays over 24 hours.

When you Sustain the spell, you can choose another unoccupied square in range that the bees move to and fill with wax shapes. Any amount of area or splash damage to the square they're present in kills the bees, ending further construction.

**Source:** `= this.source` (`= this.source-type`)
