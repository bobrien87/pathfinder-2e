---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Holy]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "10-foot square"
defense: "Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You summon a small, fluffy white nimbus cloud that floats 10 feet above the ground and rains down pleasantly warm sanctified water. The rain deals 5d6 spirit damage to fiends, undead, and creatures that have a weakness to spirit damage in the area at the end of your turn. When you Sustain the spell, you can move the cloud at a fly speed of 15 feet to anywhere in the spell's range. The water dissipates as it makes contact with any creatures or surfaces, leaving only a bit of humidity in its place.

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
