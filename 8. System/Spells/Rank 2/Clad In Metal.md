---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 metal object of 5 Bulk or less that's unattended or attended by a willing creature"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You briefly swap the outer surface of the metal in an object with a suitable amount of a common precious metal from the Plane of Metal. You can instead choose an uncommon or rare metal if you have access to it or the GM has given you access to it.

The object functions as an item of that metal, provided the item would be 2nd level or lower. For example, you could make a dagger into a cold iron or silver dagger (2nd-level items) but couldn't make full plate into cold iron armor or silver armor (5th-level items). This imparts any special properties of the precious metal—a weapon clad in cold iron activates weaknesses to cold iron, for example—and suppresses any special properties of the original metal of which the item was made.

The spell neither changes the structural integrity of the item nor damages it. The object can pass a cursory inspection, but the magical effect is obvious to anyone who studies the item closely, so it doesn't alter the Price of the item if you attempt to sell it.

**Heightened (+1)** The maximum level of the precious metal increases by 2.

**Source:** `= this.source` (`= this.source-type`)
