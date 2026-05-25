---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "500 feet"
area: "10-foot burst"
defense: "Reflex"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You grasp a piece of the landscape—such as a tree, carriage, or piece of masonry—and lob it in your foe's direction. Your missile crashes down in either a @Template[type:burst|distance:10] (for most missiles) or a @Template[type:line|distance:30] (for something long and tall, like a tree or a ship's mast), dealing @Damage[14d6[bludgeoning]|options:area-damage] damage and turning its area into difficult terrain as it breaks into rubble. All creatures in the area must attempt a Reflex save. If the area is a line, it doesn't have to start from your square but can instead start anywhere in range, as long as the entire area remains within range.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is knocked [[Prone]].
- **Critical Failure** The creature takes double damage, is knocked prone, and is [[Stunned]] 1.

**Heightened (+1)** The damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
