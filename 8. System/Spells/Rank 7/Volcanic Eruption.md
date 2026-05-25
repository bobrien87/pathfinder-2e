---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "5-foot cylinder"
defense: "Reflex"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 5-foot radius, 80-foot-tall cylinder

The ground opens up, spraying a column of lava high into the air in a vertical cylinder, dealing 14d6 fire damage to creatures in the area. The lava rapidly cools and encases creatures in the area. A creature encased in rock is [[Clumsy]] 1 and takes a –10-foot status penalty to its Speeds. All normal terrain is difficult terrain to a flying creature, and such creatures immediately descend 20 feet the moment they're encased, but they don't take damage from this fall. A creature encased in rock can attempt to [[Escape]] against your spell DC to end the effect. Otherwise, the creature remains encased until it takes a total of 50 damage, freeing it from the rock. Additionally, creatures in the area and those within 5 feet of the lava column automatically take @Damage[(@item.rank -4)d6[fire]] damage from the intense heat, regardless of the results of their saving throws.

> [!danger] Effect: Spell Effect: Volcanic Eruption
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is encased.
- **Critical Failure** The creature takes double damage and is encased.

**Heightened (+1)** The damage in the area increases by 2d6, and the damage from the intense heat increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
