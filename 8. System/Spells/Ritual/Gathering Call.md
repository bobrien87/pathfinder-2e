---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "7"
traits: ["[[Teleportation]]"]
cast: "7 days"
range: "20 feet"
targets: "up to seven willing creatures of 14th level or lower"
duration: "1 year"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You bind yourself and your allies to the specific safe location, referred to as a sanctuary, where you perform the ritual. This allows the participants to return later by simply speaking a word.
- **Success** You form the connection with the sanctuary. Any participant in the ritual can Dismiss the ritual. When they do, all the participants can immediately return to the sanctuary from any distance, as long as they are on the same plane as the sanctuary. Each participant arrives in the position in which they were standing during the casting of the ritual. When the word is spoken, all other participants know it, and each can choose whether or not to return to the sanctuary at that time. The ritual then immediately ends.
- **Failure** You fail to form the connection between the participants and the sanctuary and are aware that the ritual has failed.
- **Critical Failure** The ritual inadvertently forms a connection with a location on another plane. The casters are unaware of this misalignment. When the word is invoked, all ritual participants are shifted to this extraplanar location.

**Heightened (+1)** The cost increases by 5,000 gp, the ritual can target one more creature, and the maximum level of creature it can target increases by 2.

**Source:** `= this.source` (`= this.source-type`)
