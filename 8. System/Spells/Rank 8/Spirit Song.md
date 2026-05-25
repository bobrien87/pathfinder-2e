---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Spirit]]"]
cast: "`pf2:2`"
area: "60-foot cone"
defense: "basic Fortitude"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your eldritch song sends pulsing waves of ethereal energy to attack creatures' spirits in the area, dealing 14d6 spirit damage that causes their bodies to momentarily freeze up from the hypnotic nature of the tune, depending on the result of their Fortitude save. The vibrating waves of spirit song penetrate into, but not through, solid barriers, damaging incorporeal creatures hiding in solid objects in the area but not passing onward to damage creatures in other rooms.
- **Critical Success** The creature takes no damage.
- **Success** The creature takes half damage and can't use reactions until the beginning of its turn.
- **Failure** The creature takes full damage, can't use reactions until the beginning of its turn, and is [[Stunned]] 1.
- **Critical Failure** The creature takes double damage, can't use reactions until the beginning of its turn, and is [[Stunned]] 2.

**Heightened (+1)** The damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
