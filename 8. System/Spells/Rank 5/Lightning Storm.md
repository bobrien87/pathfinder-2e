---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Electricity]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "20-foot burst"
defense: "basic Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a black, rumbling storm cloud and call down one lightning bolt within the spell's area. The bolt is a vertical line from the top of the storm cloud to the ground below, dealing 4d12 electricity damage to creatures in the line (basic Reflex save). On subsequent rounds, the first time you Sustain the Spell each round, you can call another lightning bolt within the area. If you Cast this Spell outdoors, you can create two non-overlapping clouds instead of one, though you can still call down only one bolt per turn.

**Heightened (+2)** The damage of each bolt increases by 1d12.

**Source:** `= this.source` (`= this.source-type`)
