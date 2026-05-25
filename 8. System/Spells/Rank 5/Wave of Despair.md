---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "30-foot cone"
defense: "Will"
duration: "1 or more rounds"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You inflict despair on creatures in the area. The effects for each creature are determined by its Will save.
- **Critical Success** The creature is unaffected.
- **Success** For 1 round, the creature can't use reactions and must attempt another save at the start of its turn; on a failure, it is [[Slowed]] 1 for that turn as it sobs uncontrollably.
- **Failure** As success, but the duration is 1 minute.
- **Critical Failure** As failure, and the creature is automatically slowed 1 for 1 minute.

**Heightened (7th)** The area increases to a 60-foot cone.

**Source:** `= this.source` (`= this.source-type`)
