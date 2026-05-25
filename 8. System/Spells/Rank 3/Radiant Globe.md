---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "10-foot burst"
defense: "Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a dome of brilliant light that destroys projectiles attempting to pass through it. Ammunition from physical ranged attacks—such as arrows, bolts, sling bullets, and other objects of similar size—is destroyed in a flash of light when it passes into or out of the globe's area. Attackers targeting creatures or objects through the globe's surface with physical ranged attacks must succeed at a Fortitude save or become [[Dazzled]] for 1 round ([[Blinded]] for 1 round on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
