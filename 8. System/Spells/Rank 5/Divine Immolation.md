---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]", "[[Sanctified]]", "[[Spirit]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "20-foot burst"
defense: "basic Reflex"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Divine flames scour creatures within the area. Creatures take 6d6 fire damage and @Damage[(@item.level -3)d6[persistent,fire]] damage. The divine power within the flames scorches the spirit as well; a creature takes spirit damage instead of fire damage from divine immolation if that would be more detrimental to the creature (as determined by the GM).
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and no persistent damage.
- **Failure** The creature takes full damage and persistent damage.
- **Critical Failure** The creature takes double damage and double persistent damage.

**Heightened (+1)** The damage increases by 1d6 and persistent damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
