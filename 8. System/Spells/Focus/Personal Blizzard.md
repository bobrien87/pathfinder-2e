---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Cold]]", "[[Focus]]", "[[Hex]]", "[[Witch]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature"
defense: "Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your patron's breath becomes blizzard of obscuring, scouring ice that follows your target. The target attempts a Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target takes 1d6 cold damage, and the spell ends.
- **Failure** The target takes 1d6 cold damage and 1d6 persistent,cold damage. The persistent damage automatically ends when the spell ends. It is [[Concealed]] to other creatures, and other creatures are concealed to it.
- **Critical Failure** As failure, but both the cold damage and the persistent cold damage increase to 2d6.

**Heightened (+1)** The cold damage and persistent cold damage increase by 1 (2 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
