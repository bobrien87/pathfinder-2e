---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]", "[[Prediction]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
duration: "1 hour"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You gain a sixth sense that warns you of danger that might befall the target of the spell. If you choose a creature other than yourself as the target, you create a psychic link through which you can inform the target of danger. This link is a mental effect. Due to the amount of information this spell requires you to process, you can't have more than one *foresight* spell in effect at a time. Casting *foresight* again ends the previous *foresight*. While *foresight* is in effect, the target gains a +2 status bonus to initiative rolls and isn't [[Off Guard]] against [[Undetected]] creatures or when flanked. In addition, you gain the following reaction: [[Foresight]]

> [!danger] Effect: Spell Effect: Foresight

**Source:** `= this.source` (`= this.source-type`)
