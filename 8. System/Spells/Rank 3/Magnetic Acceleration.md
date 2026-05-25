---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature or object"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You magnetize a small metal object, such as a nail or coin, and launch it away from you at massive speed. Make a ranged spell attack roll; if the target is wearing metal armor or is made of metal, you gain a +1 circumstance bonus to your attack roll with *magnetic acceleration*. On a hit, the target takes 3d6 bludgeoning damage and 3d6 piercing damage, or double damage on a critical hit.

**Heightened (+1)** The bludgeoning and piercing damage each increase by 1d6.

**Source:** `= this.source` (`= this.source-type`)
