---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "10 minutes"
range: "5 feet"
targets: "up to 8 willing creatures"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Requirements** You have a planar key for the destination plane, used as a locus

You and your allies traverse the barriers between planes of existence. The targets move to another plane, such as the Plane of Fire, the Netherworld, or the Outer Rifts. You must know the destination plane exists and use a magic planar key created from material from that plane as a locus for the spell. While the planar keys for most prominent planes are uncommon, just like the spell *interplanar teleport*, more obscure planes and demiplanes often have rare or possibly even unique planar keys.

The spell is highly imprecise, and you appear 1d20×25 miles from the last place one of the targets (of your choice) was located the last time that target traveled to the plane. If it's the first time traveling to a particular plane for all targets, you appear at a random location on the plane. *Interplanar teleport* doesn't provide a means of return travel, though casting *interplanar teleport* again allows you to return to your previous plane unless there are extenuating circumstances.

**Source:** `= this.source` (`= this.source-type`)
