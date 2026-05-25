---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Death]]", "[[Manipulate]]", "[[Void]]"]
cast: "`pf2:2`"
area: "60-foot line"
defense: "Fortitude"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You unleash a wave of death to snuff out the life force of those in its path. Each living creature of 17th level or lower in the line must attempt a Fortitude save. If the damage from *massacre* reduces a creature to 0 Hit Points, that creature dies instantly. If *massacre* doesn't kill even a single creature, the void energy hungrily turns backward toward you, dealing an additional 30 void damage to every living creature in the line (even those above 17th level) and 30 void damage to you.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes 9d6 void damage.
- **Failure** The creature takes @Damage[(ternary(gte(@item.rank,10),115,100))[void]] damage.
- **Critical Failure** The creature dies.

**Heightened (10th)** The spell can affect living creatures up to 19th level. Increase the damage to 10d6 on a success, and to 115 on a failure.

**Source:** `= this.source` (`= this.source-type`)
