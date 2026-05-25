---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Hex]]", "[[Sonic]]", "[[Witch]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The target feels the brush of feathers against its skin and hears screeches in its ears, warning it to keep away from a creature you designate that's within 30 feet of you when you Cast this Spell (which can include yourself). Once per round, if the target moves closer to the designated creature, it must attempt a Will save or take @Damage[(@item.rank)d4[piercing]] or @Damage[(@item.rank)d4[sonic]] damage.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage.
- **Failure** The target takes full damage.
- **Critical Failure** The target takes @Damage[(@item.rank)d4[sonic],(@item.rank)d4[piercing]] damage, and if it attempts an attack roll or hostile skill check this round, it takes a –2 status penalty to the roll.

> [!danger] Effect: Spell Effect: Murmuration

**Heightened (+1)** The damage increases by 1d4, or by 2d4 on a critical failure (1d4 of which is sonic and 1d4 of which is piercing).

**Source:** `= this.source` (`= this.source-type`)
