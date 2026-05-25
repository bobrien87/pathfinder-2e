---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "120-foot line"
defense: "Fortitude"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A jagged crack opens in the air, dealing 12d8 cold damage as it draws away warmth. Each creature along the rift must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Slowed]] 1 until the start of your next turn.
- **Critical Failure** The creature takes double damage, is [[Immobilized]] by a layer of ice, and is slowed 1 as long as it's immobilized. The ice is an object with 60 Hit Points, Hardness 5, immunity to cold damage, and vulnerability 10 to fire. It has object immunities and is destroyed if the target Escapes.

**Heightened (+1)** The damage increases by 1d8 and the ice's Hit Points increase by 5.

**Source:** `= this.source` (`= this.source-type`)
