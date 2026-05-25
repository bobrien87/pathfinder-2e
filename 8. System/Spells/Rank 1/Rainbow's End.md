---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Light]]", "[[Manipulate]]", "[[Mythic]]", "[[Spirit]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "10-foot burst"
defense: "basic Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You reach upward to wrest down a rainbow and harness its power to connect this world to the heavens. Each creature in the area takes 1d4 spirit damage with a basic Fortitude save. Any creature that fails this save is additionally [[Dazzled]] for 1 round. For the spell's duration, an ally who's adjacent to you can Interact and be instantly teleported to an unoccupied space in the spell's area, as long as they don't travel more than 60 feet. This effect has the teleportation trait.

**Heightened (+2)** The damage increases by 2d4, the duration of the dazzled condition on a failed save increases by 1 round, and the maximum distance an ally can use the rainbow to teleport increases by 10 feet.

**Source:** `= this.source` (`= this.source-type`)
