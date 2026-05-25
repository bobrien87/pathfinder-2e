---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]", "[[Poison]]"]
cast: "`pf2:2`"
defense: "Fortitude"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your form ripples as you take on the fluidity and toxicity of quicksilver. You partially shift into a liquid metal form and Stride up to twice your speed. During this movement, you can pass through one creature's space—without needing to attempt a check to [[Tumble Through]]—by splitting into droplets of mercury and reforming on the other side, though you can't end your turn in such a space. Passing through a creature's space in this way exposes it to mercury poisoning, with a Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target becomes [[Sickened]] 1.
- **Failure** The target becomes [[Sickened]] 2 and takes @Damage[(@item.level+2)d6[poison]] damage.
- **Critical Failure** The target becomes [[Sickened]] 2 and takes @Damage[((@item.level+2)*2)d6[poison]] damage.

**Heightened (+1)** The damage increases by 1d6 on a failure and 2d6 on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
