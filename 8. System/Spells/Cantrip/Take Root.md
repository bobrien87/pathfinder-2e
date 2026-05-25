---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 willing creature"
duration: "1 round"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Roots sprout from the flesh of the target and coil across the floor or around objects, reinforcing their stance or grip. The targeted creature gains a +1 circumstance bonus to their Fortitude DC against attempts to [[Shove]] them and a +1 circumstance bonus to their Reflex DC against attempts to [[Disarm]] or [[Trip]] them. This bonus also applies to saving throws against spells or effects that would attempt to remove a held item from their grasp.

> [!danger] Effect: Spell Effect: Take Root

**Source:** `= this.source` (`= this.source-type`)
