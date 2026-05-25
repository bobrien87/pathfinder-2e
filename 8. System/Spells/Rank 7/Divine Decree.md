---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Sanctified]]", "[[Spirit]]"]
cast: "`pf2:2`"
area: "40-foot emanation"
defense: "Fortitude"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You utter a potent litany from your faith, a mandate that harms those who oppose your ideals. You deal 7d10 spirit damage to your enemies in the area; each enemy must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Enfeebled]] 2 for 1 minute.
- **Critical Failure** The creature takes double damage and is enfeebled 2 for 1 minute. If you're on your home plane and the creature is not, the creature is sent back to its home plane. A creature of 10th level or lower must also succeed at a Will save or be [[Paralyzed]] for 1 minute; if it critically fails, it dies (this is a death effect).

**Heightened (+1)** The damage increases by 1d10, and the level of creatures that must attempt a second save on a critical failure increases by 2.

**Source:** `= this.source` (`= this.source-type`)
