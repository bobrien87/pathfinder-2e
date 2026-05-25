---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Light]]", "[[Manipulate]]", "[[Vitality]]"]
cast: "`pf2:2`"
range: "500 feet"
area: "60-foot burst"
defense: "Reflex"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A powerful globe of chilling moonlight explodes in the area, dealing 8d10 cold damage to all creatures in the area, plus an additional @Damage[(@item.rank+1)d10[vitality]] damage to undead creatures.

*Moonburst*'s cold damage is silver damage for the purposes of weaknesses, resistances, and the like. Each creature and object in the area must attempt a Reflex save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage.
- **Critical Failure** The creature takes full damage and becomes [[Blinded]] permanently.

If the globe overlaps with an area of magical darkness, *moonburst* attempts to counteract the darkness effect.

**Heightened (+1)** The cold damage increases by 1d10, and the vitality damage against undead increases by 1d10.

**Source:** `= this.source` (`= this.source-type`)
