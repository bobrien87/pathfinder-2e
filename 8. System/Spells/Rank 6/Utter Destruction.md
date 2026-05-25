---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Death]]", "[[Sonic]]", "[[Void]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "30-foot cone"
defense: "Fortitude"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You screech with an unearthly voice made of destructive energy, smashing everything that lies before you. Creatures in the area take 4d8 sonic damage and 4d8 void damage. Each creature must attempt a Fortitude save. Unattended objects of Hardness 5 or less in the area of effect are destroyed.
- **Critical Success** The creature takes half damage.
- **Success** The creature takes half damage and is [[Deafened]] for 1 round.
- **Failure** The creature takes full damage and is deafened for 1 minute.
- **Critical Failure** The creature takes double damage and is permanently deafened.

**Heightened (+1)** The sonic and void damage each increase by 1d8. The Hardness threshold of items destroyed by the spell increases by 1.

**Source:** `= this.source` (`= this.source-type`)
