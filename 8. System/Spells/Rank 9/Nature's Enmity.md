---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "500-foot burst"
targets: "up to 5 creatures"
defense: "Reflex"
duration: "10 minutes"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Animals, plants, and fungi in the area turn against the targets. Each target suffers from the following effects as long as it remains in the area.

- Vegetation springs up from every surface, giving each target a –10-foot circumstance penalty to its Speed any time it's adjacent to the plants and fungi.
- Aggressive animals attack unpredictably. At the start of its turn, each target rolls a DC 8 flat check. On a failure, it's attacked by creatures that deal 2d10 slashing damage. The target attempts a basic Reflex save and is [[Off Guard]] for 1 round on any outcome other than a critical success.
- The target loses any connection to nature or natural creatures. The target must succeed at a DC 5 flat check when casting any primal spell or the spell fails. Furthermore, animal, fungus, and plant creatures become hostile to it, even one with a strong bond to the target, such as an animal companion.

The GM might decide that you can't subject some creatures, such as an emissary of a nature deity, to the ire of nature.

**Source:** `= this.source` (`= this.source-type`)
