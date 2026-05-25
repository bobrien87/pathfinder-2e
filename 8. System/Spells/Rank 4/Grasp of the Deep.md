---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]", "[[Water]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You grip one target with the phantasmal pressure of the deep sea, disorienting and crushing its lungs and joints. The target takes 6d6 bludgeoning damage and other effects, depending on its Will saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The target takes half damage.
- **Failure** The target takes full damage, and feels as though it's being crushed. The target also becomes [[Grabbed]], but it can attempt to [[Escape]] with an Escape DC equal to your spell DC.
- **Critical Failure** As failure, but the target takes double damage.

**Heightened (6th)** You can target up to 5 creatures.

**Source:** `= this.source` (`= this.source-type`)
