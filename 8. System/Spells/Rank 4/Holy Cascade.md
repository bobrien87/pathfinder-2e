---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Holy]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:2`"
range: "500 feet"
area: "20-foot burst"
defense: "basic Reflex"
requirements: "one vial of holy water"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon sacred energy to amplify a vial of [[Holy Water]], tossing it an incredible distance. It explodes in an enormous burst that deals 3d6 bludgeoning damage to creatures in the area from the cascade of water. The water deals an additional @Damage[((@item.level*2)-2)d6[spirit]] damage to creatures with the unholy trait in the area.

**Heightened (+1)** The bludgeoning damage increases by 1d6, and the additional spirit damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
