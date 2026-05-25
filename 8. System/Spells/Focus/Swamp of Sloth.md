---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Olfactory]]", "[[Sorcerer]]"]
cast: "1 to 3"
range: "120 feet"
defense: "basic Fortitude"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Ground in the area turns swampy and fetid. The area is difficult terrain. The sludge at the bottom of the morass animates into diminutive sludge beasts that have a demonic appearance. These don't function as normal creatures, but they swarm over creatures in the swamp and exude a noxious stench. The swamp deals 1d6 poison damage to creatures that end their turn in the area (basic Fortitude save). For each additional action you use when Casting the Spell, increase the burst's radius by 5 feet.

**Heightened (+2)** The damage increases by 1d6, and the initial radius increases by 5 feet

**Source:** `= this.source` (`= this.source-type`)
