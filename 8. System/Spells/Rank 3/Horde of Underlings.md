---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
area: "30-foot cone"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You summon six underlings, such as skeletons or kobolds. When you cast this spell, you decide what kind of creatures they are, if they're Small or Medium, and whether they deal bludgeoning, piercing, or slashing damage (choose once and applying it to all underlings). Each underling has 1 Hit Point, 5 AC, and automatically fails all saving throws. Each underling appears in an unoccupied square of your choice within the area. The underlings don't block movement, but they are difficult terrain for creatures other than you.

Each underling attacks one enemy adjacent to it (if any), automatically dealing 1d4 damage of the chosen type. The first time you Sustain the spell on each subsequent round, each underling moves 20 feet toward the nearest enemy. If an underling ends its movement adjacent to an enemy, it damages that enemy as described above.

**Heightened (+1)** The number of underlings increases by 2

**Source:** `= this.source` (`= this.source-type`)
