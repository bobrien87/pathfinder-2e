---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Earth]]", "[[Fire]]", "[[Focus]]"]
cast: "`pf2:1`"
range: "30 feet"
area: "10-foot burst"
defense: "basic Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your apparition is the will of lava and magma made manifest, the earth's molten blood unleashing devastating bursts of liquid stone and unquenchable fire at your command. When you Cast this Spell and the first time you Sustain it each round thereafter, choose an area within range. Each creature in the area takes 1d4 fire damage, 1d4 bludgeoning damage, and @Damage[(ceil(@item.rank/2))[persistent,fire]] damage (the persistent fire damage is negated on a successful save).

**Heightened (+2)** The fire and bludgeoning damage each increase by 1d4, and the persistent fire damage increases by 1.

**Source:** `= this.source` (`= this.source-type`)
