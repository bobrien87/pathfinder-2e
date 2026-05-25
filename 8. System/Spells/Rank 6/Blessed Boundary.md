---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Force]]", "[[Manipulate]]", "[[Sanctified]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "60-foot burst"
defense: "basic Reflex"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Manifestations of divine force appear in the hundreds, swirling in a massive, protective sphere. These typically look like spiky fragments, but often take on an appearance themed to the deity of the caster. The sphere is hollow, with the manifestations forming a shell 2 inches deep on the outer edge. You can choose to make the burst smaller, in 5-foot increments, when you cast it. The shell provides cover and can intersect solid terrain without affecting it. The shell deals 7d8 force damage to each creature who intersects with the shell when the sphere's created, or who attempts to move through the shell. The creature also takes the damage at the end of its turn, but only if it didn't already take damage from the shell that turn. The effects are determined by a creature's Reflex save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage, is pushed up to 10 feet in the direction of your choice, and ends its movement.
- **Critical Failure** The creature takes double damage, is pushed up to 20 feet in the direction of your choice, and ends its movement.

**Heightened (+1)** The damage increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
