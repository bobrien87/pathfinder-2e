---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "up to 4 willing creatures"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The scene would play out exactly as you envisioned it, if only the actors would respect their blocking. You instantly transport the targeted creatures and any items they're wearing and holding from their current space to an unoccupied space within range. You don't need to be able to see the destinations as long as you've been there in the past and know its relative location and distance from each target. Creatures affected by take your places are then temporarily immune to this spell for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
