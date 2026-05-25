---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "60-foot cone"
defense: "Fortitude"
duration: "varies"
source: "Pathfinder #212: A Voice in the Blight"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a cone of shimmering energy that attempts to banish the influence of invasive, supernatural blight, such as that found in Tanglebriar. Blighted difficult terrain in the area becomes regular terrain, while blighted greater difficult terrain becomes difficult terrain; hazardous terrain in the area becomes nonhazardous. These effects persist for 1 hour.

Creatures in the area that carry features of this blight (as determined by the GM, but automatically including all creatures with the fiend trait in this adventure) are trimmed as well, their supernatural infusion of blight being drained. These creatures take 12d10 spirit damage and must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature's reach with attacks is reduced by 5 feet (to a minimum of 5 feet) for 1 hour, they are [[Sickened]] 1 and [[Slowed]] 1 for 1 round.
- **Critical Failure** The creature's reach is reduced to 5 feet for 1 hour, they are [[Sickened]] 2 and slowed 1 for 1 minute.

**Heightened (10th)** The spirit damage increases by 2d10, and 1 hour durations increase to 24 hours.

**Source:** `= this.source` (`= this.source-type`)
