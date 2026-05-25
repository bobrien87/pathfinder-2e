---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Manipulate]]"]
cast: "`pf2:1`"
duration: "until the end of your turn"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a beacon in time to return to it if things go wrong. You can cast *time beacon* only on your turn. Keep careful track of everything that happens this turn after you cast *time beacon*. At the end of your turn, you can choose to rewind time back to just after you cast *time beacon*, removing all effects of your turn since then. Curses, traps, and other harmful effects that happen during your turn might prevent you from returning to the beacon if they're powerful enough. If you were affected by any harmful effects during your turn after casting *time beacon*, in order to return to your beacon, *time beacon* attempts a counteract check against each such effect. If it fails at any of these checks, you can't return. After returning to the time beacon, the spell ends.

**Source:** `= this.source` (`= this.source-type`)
