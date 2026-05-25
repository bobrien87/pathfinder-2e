---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "15-foot cone"
defense: "Reflex"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a wave of energy that ripples through the earth. Terrestrial creatures in the affected area must attempt a Reflex save to avoid stumbling as the shockwave shakes the ground.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Off Guard]] until the start of its next turn.
- **Failure** The creature falls [[Prone]].
- **Critical Failure** As failure, plus the creature takes 1d6 bludgeoning damage.

**Heightened (+1)** The area increases by 5 feet (to a 20-foot cone at 2nd rank, and so on).

**Source:** `= this.source` (`= this.source-type`)
