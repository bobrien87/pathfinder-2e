---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Focus]]", "[[Manipulate]]", "[[Oracle]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "20-foot burst"
defense: "Fortitude"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A cloud of magical ashes descends upon creatures in the area. The ashes scour flesh and linger in the wounds, igniting upon the slightest flicker of flame. Creatures in the area take 4d6 slashing damage and must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and has weakness to fire 3 until the start of its next turn.
- **Failure** The creature takes full damage and has weakness to fire 3 for 1 minute. If the creature is killed by fire during this time it's reduced to ashes, though its gear remains.
- **Critical Failure** As failure, except the creature takes double damage.

**Heightened (+1)** The slashing damage increases by 2d6 and weakness to fire increases by 1.

> [!danger] Effect: Spell Effect: Incendiary Ashes (Success)

> [!danger] Effect: Spell Effect: Incendiary Ashes (Failure)

**Source:** `= this.source` (`= this.source-type`)
