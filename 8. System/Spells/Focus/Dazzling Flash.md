---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Light]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:2`"
area: "15-foot cone"
defense: "Fortitude"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You raise your religious symbol and create a blinding flash of light. Each creature in the area must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] for 1 round.
- **Failure** The creature is [[Blinded]] for 1 round and Dazzled for 1 minute. The creature can spend an Interact action rubbing its eyes to end the Blinded condition.
- **Critical Failure** The creature is Blinded for 1 round and Dazzled for 1 hour.

**Heightened (3rd)** The area increases to a 30-foot cone.

**Source:** `= this.source` (`= this.source-type`)
