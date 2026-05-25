---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "1 hour"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Webbing grows between your fingers and your nails extend into vicious claws. For the spell's duration, you gain a +1 status bonus to Athletics checks to Swim and you gain a claws unarmed attack. They're an agile, finesse, unarmed attack that deals 1d4 slashing damage and an additional 1d6 cold damage.

> [!danger] Effect: Spell Effect: Claws of the Otter

**Heightened (+3)** The additional cold damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
