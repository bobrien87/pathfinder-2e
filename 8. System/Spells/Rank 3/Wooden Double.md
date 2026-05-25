---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Manipulate]]", "[[Wood]]"]
cast: "`pf2:r`"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You're critically hit by a damage-dealing effect or a Strike.

A wooden double appears out of nowhere and takes the blow in your place. Take a Step action. A wooden block of your size and roughly shaped like you appears in the space you left and absorbs the hit. This block has Hardness 5 and 20 Hit Points. If the wooden block is destroyed, you take any excess damage that the block didn't absorb. After taking the blow, the wooden block collapses into a pile of splinters and dust.

**Heightened (+1)** The block's Hit Points increase by 10.

**Source:** `= this.source` (`= this.source-type`)
