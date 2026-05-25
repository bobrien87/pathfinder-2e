---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "500 feet"
area: "60-foot burst"
defense: "basic Reflex"
duration: "1 round"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You shake the ground, topple creatures into fissures, and collapse structures. The GM might add additional effects in certain areas. Cliffs might collapse, causing creatures to fall, or a lake might drain as fissures open up below its surface, leaving a morass of quicksand.

- **Shaking Ground** The ground is difficult terrain, and creatures on it take a -2 circumstance penalty to attack rolls, AC, and skill checks. 

> [!danger] Effect: Spell Effect: Earthquake (Shaking Ground)

- **Fissures** Each creature on the ground must attempt a Reflex save at the start of its turn to keep its footing and avoid falling into 40-foot-deep fissures that open beneath it. The fissures are permanent, and their sides require successful DC 15 [[Athletics]] check to Climb.
- **Collapse** Structures and ceilings might collapse. The GM rolls a flat check for each (DC 16 flat check for a sturdy structure, DC 14 flat check for an average structure and most natural formations, DC 9 flat check for a shoddy structure, all adjusted higher or lower as the GM sees fit). A collapse deals 11d6 bludgeoning damage to each creature caught in it with a basic Reflex save. A creature falls [[Prone]] unless it critically succeeds and falls into a fissure if it critically fails.

**Heightened (10th)** You create a massive earthquake that can devastate a settlement. The range increases to half a mile and the area to a quarter-mile burst.

**Source:** `= this.source` (`= this.source-type`)
