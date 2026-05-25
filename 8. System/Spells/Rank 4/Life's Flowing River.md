---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a flowing river of ghostly water and that sheds dim light for 10 feet on each side. The river begins in an adjacent square to you and extends in a straight 5-foot path to its maximum range or until it hits a solid barrier, whichever comes first. A creature that begins its turn in the glowing waters of the river or who enters one of the river's spaces must attempt a Will save. If the creature is undead or a nindoru, it takes 4d6 mental damage, modified by the result of their Will save.
- **Critical Success** The creature ignores the river's effects until the start of its next turn. If the creature is undead or a nindoru, it takes no damage.
- **Success** The creature treats all squares occupied by the river as difficult terrain until the start of its next turn. If the creature is undead or a nindoru, it takes half damage.
- **Failure** As success, but the creature is also knocked [[Prone]]. If the creature is undead or a nindoru, it takes full damage.
- **Critical Failure** As failure, but the creature is pushed 20 feet along the river's path in the direction of flow. If the creature is undead or a nindoru, it takes double mental damage.

**Heightened (+1)** The mental damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
