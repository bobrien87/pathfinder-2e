---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
defense: "Reflex"
duration: "1 round"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You tear open the ground then slam it shut. The target creature takes 2d6 bludgeoning damage with a Reflex save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage.
- **Failure** The target takes full damage, is [[Off Guard]], and takes a –10-foot circumstance penalty to Speed.
- **Critical Failure** The target takes double damage and is off-guard and [[Immobilized]]. It can attempt to `act escape` against your spell DC. If it doesn't Escape, the target takes an additional 2d6 bludgeoning damage when the spell ends.

> [!danger] Effect: Spell Effect: Crushing Ground

**Heightened (+1)** Increase the initial damage and additional damage by 2d6.

**Source:** `= this.source` (`= this.source-type`)
