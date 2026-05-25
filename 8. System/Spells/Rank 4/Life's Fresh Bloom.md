---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Manipulate]]", "[[Vitality]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "20-foot burst"
defense: "Fortitude"
duration: "5 rounds (sustained)"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The ground around you blooms with life, sprouting sparkling grass, flowers, and small shrubs. Each living and non-nindoru creature that starts its turn standing on the ground in the area recovers 1d6 Hit Points and gains a +5-foot status bonus to its Speed until the end of its next turn. Nindoru fiends and undead that start their turn in the area of life's fresh bloom instead become [[Sickened]] 1 unless they succeed at a Fortitude saving throw.

> [!danger] Effect: Spell Effect: Life's Fresh Bloom

**Heightened (7th)** Increase the Hit Points restored to 1d8 and [[Sickened]] 2.

**Heightened (10th)** Increase the Hit Points restored to 1d10 and [[Sickened]] 3.

**Source:** `= this.source` (`= this.source-type`)
