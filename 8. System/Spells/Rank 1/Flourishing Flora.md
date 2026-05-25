---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "5-foot burst"
defense: "basic Reflex"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Plants rapidly grow up from the ground. All creatures in the target area take 2d4 damage. The type of damage depends on the type of plant you choose to grow. On a critical failure, targets experience additional effects, also depending on what you choose to grow. The type of plant and its effects are chosen when you Cast the Spell.

- **Cacti** Piercing damage, and @Damage[(@item.level)[bleed]] damage on a critical failure.

- **Flowers** Poison damage, and [[Dazzled]] for 2 rounds on a critical failure.

- **Fruits** Bludgeoning damage, and [[Clumsy]] 1 for 2 rounds on a critical failure.

- **Roots** Bludgeoning damage, and the affected creatures fall [[Prone]] on a critical failure.

**Heightened (+1)** The damage increases by 1d4, and the persistent bleed damage from cacti increases by 1.

**Source:** `= this.source` (`= this.source-type`)
