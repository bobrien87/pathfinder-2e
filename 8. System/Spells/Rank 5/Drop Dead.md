---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Illusion]]", "[[Manipulate]]", "[[Subtle]]", "[[Visual]]"]
cast: "`pf2:r`"
range: "120 feet"
targets: "1 creature"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** A creature within range is hit by an attack from an enemy.

The target appears to fall down dead, though it actually turns [[Invisible]]. Its illusory corpse remains where it fell, complete with a believable fatal wound. This illusion looks and feels like a dead body. If the target's death seems absurd—for instance, a barbarian at full health appears to be slain by 2 damage—the GM can grant the attacker an immediate [[Perception]] check to disbelieve the illusion. If the target uses hostile actions, the spell ends. This ends the entire spell, so the illusory corpse disappears too.

**Heightened (7th)** The spell doesn't end if the target uses a hostile action.

**Source:** `= this.source` (`= this.source-type`)
