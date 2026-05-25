---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Cold]]", "[[Inventor]]", "[[Manipulate]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You vent a jet of supercooled fluid from your innovation, damaging a foe and slowing it down. Target one creature within 60 feet. That creature takes @Damage[@actor.level[cold]]{cold damage equal to your level}, with effects depending on its [[Reflex]] save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage and takes a –5-foot status penalty to its Speeds for 1 round.
- **Failure** The target takes full damage and takes a –10-foot status penalty to its Speeds for 1 round.
- **Critical Failure** The target takes double damage, is [[Slowed]] 1 for 1 round, and takes a –15-foot status penalty to its Speeds for 1 round.

> [!danger] Effect: Deep Freeze

**Unstable Function** Your innovation discharges an enormous cone of supercooled fluid, potentially causing cascading failures. Add the unstable trait to Deep Freeze. The ability affects all creatures within a @Template[cone|distance:60] instead of a single target, and it deals @Damage[(2*@actor.level)[cold]|traits:unstable|options:area-damage]{cold damage equal to double your level} instead of equal to your level.

If you have the revolutionary innovation class feature, you can choose a @Template[cone|distance:60] or a @Template[cone|distance:90] when you use an unstable Deep Freeze.

**Special** If your innovation is a minion, it can take this action rather than you.

**Source:** `= this.source` (`= this.source-type`)
