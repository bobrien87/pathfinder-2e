---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Darkness]]", "[[Manipulate]]", "[[Void]]"]
cast: "`pf2:2`"
range: "500 feet"
area: "60-foot burst"
defense: "Reflex"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A globe of freezing darkness explodes in the area, dealing 8d10 cold damage to creatures in the area, plus an additional 8d4 void damage to living creatures. Each creature in the area must attempt a Reflex save.

If the globe overlaps with an area of magical light or affects a creature affected by magical light, *eclipse burst* attempts to counteract the light effect.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage.
- **Critical Failure** The creature takes double damage and becomes [[Blinded]] by the darkness for an unlimited duration.

**Heightened (+1)** The cold damage increases by 1d10 and the void damage against the living increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
