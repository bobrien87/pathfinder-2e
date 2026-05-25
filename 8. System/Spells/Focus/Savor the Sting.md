---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]", "[[Nonlethal]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 creature"
defense: "Will"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You inflict pain upon the target and revel in their anguish. This deals 1d4 mental damage and @Damage[(@item.level)d4[persistent,mental]] damage; the target must attempt a Will save. As long as the target is taking persistent damage from this spell, you gain a +1 status bonus to attack rolls and skill checks against the target.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage and no persistent damage.
- **Failure** The target takes full initial and persistent damage.
- **Critical Failure** The target takes double initial and persistent damage.

**Heightened (+1)** The initial damage increases by 1d4 and the persistent damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
