---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
defense: "Reflex"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 30-foot cone or 10-foot emanation

You swing a weapon you're holding, and the weapon magically multiplies into duplicates that swipe at all creatures in either a cone or an emanation. This flurry deals four dice of damage to creatures in the area. This damage has the same type as the weapon and uses the same die size. Determine the die size as if you were attacking with the weapon; for instance, if you were wielding a two-hand weapon in both hands, you'd use its two-hand damage die.
- **Critical Success** The creature is unaffected.
- **Success** The target takes half damage.
- **Failure** The target takes full damage.
- **Critical Failure** The target takes double damage and is subject to the weapon's critical specialization effect.

**Heightened (+1)** Add another damage die.

**Source:** `= this.source` (`= this.source-type`)
