---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:3`"
range: "500 feet"
area: "25-foot cylinder"
defense: "Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 25-foot radius, 20-foot tall cylinder

With a spin of your hand, you create a large swirling vortex of storming waves. All squares in the *whirlpool* are difficult terrain. The constant churning of the fierce waves means that creatures are constantly tossed between areas of air and water, allowing both air- and water-breathing creatures to breathe within the vortex. Any creature with a swim Speed can Swim instead of Stride to move within the *whirlpool*; the DC to Swim within it is equal to your spell DC.

All creatures in the area take 6d10 bludgeoning damage as the waves crash into them. On subsequent rounds, the first time you Sustain the spell each round, the waves crash again with the same effect.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is drawn 10 feet toward the center of the *whirlpool*.
- **Critical Failure** The creature takes double damage and is drawn to the center of the *whirlpool*.

**Heightened (+1)** The bludgeoning damage increases by 1d10.

**Source:** `= this.source` (`= this.source-type`)
