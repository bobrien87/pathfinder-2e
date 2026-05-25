---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "30-foot burst"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You purify the air in the area, making it clean and breathable. The spell immediately removes inhaled poisons, pollution, and similar contaminants from the air. For the remaining duration, the spell prevents any further contamination from altering air in the area, including keeping toxic air bordering the area from coming inside. (This doesn't prevent contaminants from coming in after the spell ends.) This spell doesn't create air, so casting it underwater wouldn't create breathable air, nor would it affect any toxins within air suspended in the water

**Heightened (3rd)** The area increases to 60 feet.

**Heightened (4th)** The area increases to 120 feet.

**Heightened (6th)** The area increases to 500 feet.

**Heightened (9th)** The area increases to 1 mile.

**Source:** `= this.source` (`= this.source-type`)
