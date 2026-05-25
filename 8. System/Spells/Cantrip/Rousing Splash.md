---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause a splash of cold water to descend on an ally's head, granting some temporary vigor. The target gains 1d4 temporary Hit Points, which last for 1 minute. The target is then temporarily immune to the temporary Hit Points from *rousing splash* for 10 minutes. The target can also attempt an immediate flat check to recover from a single source of persistent acid or fire damage, with the DC reduction from appropriate assistance.

**Heightened (+1)** The amount of temporary Hit Points granted increases by 1d4.

> [!danger] Effect: Spell Effect: Rousing Splash

**Source:** `= this.source` (`= this.source-type`)
