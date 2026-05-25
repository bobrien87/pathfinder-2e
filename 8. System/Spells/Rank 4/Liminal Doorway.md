---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Extradimensional]]", "[[Manipulate]]"]
cast: "10 minutes"
range: "touch"
duration: "8 hours"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You draw a chalk doorway on an unbroken surface, which opens into an extradimensional space. Any creature treating the drawing as an actual door can Interact to touch the doorknob and pass through. The warped, chalk-drawn room beyond the door is 20 feet in width, depth, and height. The space is unadorned and empty, with chalk lines indicating the corners of the walls.

If the drawing is scrubbed away, the underlying surface is broken, or a creature attempts to enter the space that would put it over capacity, the space begins to collapse. The space ejects one creature at random each round, depositing it on the nearest open ground, until all creatures are returned outside.

**Source:** `= this.source` (`= this.source-type`)
