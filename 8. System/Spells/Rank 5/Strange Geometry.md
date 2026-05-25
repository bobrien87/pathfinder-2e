---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "60 feet"
area: "10-foot cube"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 4 cubes, each 10 feet on a side

You cause the areas to appear to swell, bend, and break, twisting together in a bizarre spatial geometry. The cubes of the spell's area can't be adjacent to one another. A creature must attempt a Will save if it's in one of the cubes when you Cast the Spell, or if it later enters one of the areas, with the following effects. A creature interacting with the illusion can also attempt a Will save to disbelieve the illusion, as normal.
- **Success** The creature disbelieves the illusion.
- **Failure** All terrain in the cubes is difficult terrain for the creature, including the air if the creature is flying, walls if it's climbing, and so on. When the creature would exit one of the cubes, it exits from one randomly determined by the GM. This is a teleportation effect. It can exit from any edge of that cube it chooses. When selecting a random cube, the GM excludes any that don't match the creature's terrain; for instance, if the creature were exiting along the ground, the GM would exclude any cube that didn't have an exit on the ground.

**Source:** `= this.source` (`= this.source-type`)
