---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "15 feet"
targets: "up to 8 creatures"
duration: "10 minutes"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You shift the colors of the targets' outermost layer of clothing and gear to be closer to their environment when they remain still. Creatures affected by the spell gain a +3 status bonus to Stealth checks to Hide. The changed color granted by the spell always shifts to match the environment, even if there are drastic changes. If any piece of gear or clothing affected by the spell is removed from a creature, the spell ends for that creature.

**Heightened (6th)** If a creature affected by this spell rolls a critical failure on its Stealth check to [[Sneak]] within 30 feet of a creature that would spot it, it instead only fails its check, as the spell mildly hypnotizes the spotter.

**Heightened (8th)** As 6th rank, and the status bonus is +4.

**Source:** `= this.source` (`= this.source-type`)
