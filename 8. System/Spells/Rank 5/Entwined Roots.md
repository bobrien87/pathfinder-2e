---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Wood]]"]
cast: "1 minute"
area: "20-foot burst"
targets: "Up to 5 willing living creatures"
duration: "10 minutes"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Slithering roots gird you and your allies in layers of flexible wooden protection. Each affected creature gains resistance 5 to bludgeoning and piercing damage. Whenever a creature protected by these roots is targeted by a ranged weapon attack but takes no damage (such as if the attack missed or the damage was reduced to 0 by resistance), the roots snatch up the ammunition or thrown weapon and hold it. The protected creature can retrieve the thrown weapon or ammunition as an Interact action.

> [!danger] Effect: Spell Effect: Entwined Roots

**Heightened (7th)** The resistances increase to 10.

**Heightened (9th)** The resistances increase to 15.

**Source:** `= this.source` (`= this.source-type`)
