---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Cold]]", "[[Concentrate]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 object"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your *gelid shard* drinks down nearby heat in a futile attempt to sate itself and achieve a level of frigid cold unheard of in the Universe. This allows you to cool a drink, make a hot pot safe to handle, or other, similar minor effects. Once cooled, the object's temperature is subject to its environment as usual. You can also solidify ambient moisture into a solid object; this temporary object is of negligible Bulk, made of non-magical ice. The object looks crude and artificial and is extremely fragile—it can't be used as a tool, weapon, or locus or cost for a spell. Once created, it melts as normal for ice for the ambient conditions.

**Heightened (3rd)** You can create simple objects of ice with up to 1 Bulk and of a level not exceeding 1. Such objects must be rigid. You can only have one such object created at a time; if you create another, the previous object melts instantly.

**Heightened (5th)** Items you create can be up to 4 Bulk and 4th level.

**Heightened (7th)** Items you create can be up to 8 Bulk and 8th level.

**Heightened (9th)** Items you create can be up to 20 Bulk and 12th level.

**Source:** `= this.source` (`= this.source-type`)
