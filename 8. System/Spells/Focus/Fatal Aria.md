---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Bard]]", "[[Composition]]", "[[Concentrate]]", "[[Death]]", "[[Emotion]]", "[[Focus]]", "[[Mental]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You perform music so perfect that the target may die of joy or sorrow. Once targeted, the creature becomes temporarily immune for 1 minute. The effect of the spell depends on the target's level and current Hit Points.

**16th or Lower** The target dies instantly.

**17th** If the target has 50 Hit Points or fewer, it dies instantly; otherwise, it drops to 0 Hit Points and becomes [[Dying]] 1.

**18th or Higher** The target takes 50 untyped damage. If this brings it to 0 Hit Points, it dies instantly.

**Source:** `= this.source` (`= this.source-type`)
