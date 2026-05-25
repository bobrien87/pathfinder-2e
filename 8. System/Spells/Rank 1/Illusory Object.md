---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:2`"
range: "500 feet"
area: "20-foot burst"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create an illusory visual image of a stationary object. The entire image must fit within the spell's area. The object appears to animate naturally, but it doesn't make sounds or generate smells. For example, water would appear to pour down an illusory waterfall, but it would be silent.

Any creature that touches the image or uses the [[Seek]] action to examine it can attempt to disbelieve your illusion.

**Heightened (2nd)** Your image makes appropriate sounds, generates normal smells, and feels right to the touch. The spell gains the auditory and olfactory traits. The duration increases to 1 hour.

**Heightened (5th)** As the 2nd-rank version, but the duration is unlimited.

**Source:** `= this.source` (`= this.source-type`)
