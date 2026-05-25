---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Monk]]"]
cast: "`pf2:2`"
defense: "Fortitude"
duration: "1 month"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Make a melee unarmed Strike. If you hit and the target is alive, anytime during the duration, you can spend a single action, which has the auditory and concentrate traits, to speak a word of death that could instantly slay it. The target must attempt a Fortitude save.
- **Critical Success** The target survives, the spell ends, and the target is then temporarily immune for 24 hours.
- **Success** The target is [[Stunned]] 1 and takes @Damage[5*@item.level] damage, the spell ends, and the target is then temporarily immune for 24 hours.
- **Failure** The target is [[Stunned]] 3 and takes @Damage[10*@item.level] damage. The spell's duration continues, but the target is then temporarily immune for 24 hours against being killed by touch of death.
- **Critical Failure** The target dies.

If you cast touch of death again, the effects of any *touch of death* you had previously cast end.

**Heightened (+1)** The damage increases by 10 on a failure, or 5 on a success.

**Source:** `= this.source` (`= this.source-type`)
