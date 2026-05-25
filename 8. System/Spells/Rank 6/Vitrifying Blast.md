---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "15-foot cone"
defense: "Reflex"
duration: "varies"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You launch a cone of glass shards, which embed in creatures to turn them partially to glass. The shards deal 8d6 piercing damage to creatures in the area, based on each creature's saving throw.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage and gains weakness 3 to sonic and bludgeoning damage for 1 round.
- **Failure** The target takes full damage, is [[Slowed]] 1, and gains weakness to sonic and bludgeoning damage. The weakness is equal to 3 × the slowed value it has from this spell. The target must attempt a Fortitude save at the end of each of its turns; this ongoing save has the incapacitation trait. On a failed save, the creature's slowed value increases by 1 (or by 2 on a critical failure), to a maximum of [[Slowed]] 3. A successful save reduces the creature's slowed value by 1 (or by 2 on a critical success). If the creature ends its turn with a slowed value of 0, the effect ends.
- **Critical Failure** As failure, but the target is initially [[Slowed]] 2.

> [!danger] Effect: Spell Effect: Vitrifying Blast

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
