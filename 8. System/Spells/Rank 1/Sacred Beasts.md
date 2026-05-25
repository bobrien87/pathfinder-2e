---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "5-foot burst"
defense: "basic Reflex"
requirements: "You worship a deity."
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Requirements** You worship a deity.

You call out to the creatures of the wild favored by your deity. You quickly summon your deity's sacred animal (or a small swarm of them if the animal is usually Tiny). For example, you would call forth a lion if you worship Iomedae or a swarm of spiders if you worship Norgorber. If your deity doesn't have a known sacred animal, work with the GM to find a thematic one. The animal or swarm assaults all creatures in the area, dealing 2d6 damage. The damage is either bludgeoning, piercing, or slashing based on the animal that was conjured, as determined by the GM. After their attacks, the animals return to your deity's plane.

**Heightened (+1)** The damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
