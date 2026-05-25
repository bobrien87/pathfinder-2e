---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "20-foot burst"
defense: "Reflex"
duration: "1 minute"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause long, serrated mantis limbs to appear, swiping at and obstructing creatures in the area. The area is difficult terrain. Each creature in the area when the spell is cast and who end their turn within the area take 3d6 slashing damage and @Damage[(floor((@item.level -1)/2)d6)[bleed]] damage, as determined by its Reflex save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and no persistent damage.
- **Failure** The creature takes full damage and a –10-foot circumstance penalty to their Speed until they receive magical healing or benefit from a successful Medicine check against your spell DC to [[Administer First Aid]].
- **Critical Failure** The creature takes double damage and a –15-foot circumstance penalty to their Speed until they receive magical healing or benefit from a successful Medicine check against your spell DC to administer First Aid.

**Heightened (+2)** The damage increases by 3d6, and the persistent bleed damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
