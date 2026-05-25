---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:2`"
range: "100 feet"
defense: "Fortitude"
duration: "12 hours"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** four unoccupied 5-foot squares, each of which is at least 20 feet apart

You cultivate four wooden bulbs, each filled with toxic pollen and sensitive to motion. When a creature enters a space adjacent to a bulb, or when a bulb is touched or damaged (each bulb has AC 5), the bulb blossoms and releases pollen in a @Template[emanation|distance:15]. Creatures in the area take 8d8 poison damage and must attempt a Fortitude save with the following results.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and becomes [[Dazzled]] for 1 round.
- **Failure** The creature takes full damage, becomes dazzled for 1 round, and becomes [[Stupefied 1]] for 1 minute.
- **Critical Failure** The creature takes double damage, is dazzled for 1 round, and becomes [[Stupefied 2]] for 1 minute.

**Heightened (+1)** The damage increases by 2d8.

**Source:** `= this.source` (`= this.source-type`)
