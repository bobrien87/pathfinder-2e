---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "10-foot burst"
defense: "basic Reflex"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You raise a pair of towering waves and slam them into each other, crushing creatures caught between them. Creatures in the area take 5d6 bludgeoning damage with a basic Reflex save.

**Heightened (+1)** Increase the damage by 2d6.

**Source:** `= this.source` (`= this.source-type`)
