---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Manipulate]]"]
cast: "10 minutes"
range: "10 feet"
targets: "1 dead creature of 13th level or lower"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You attempt to call forth the dead creature's soul, requiring the creature's body to be present and relatively intact. The creature must have died within the past 3 days. If Pharasma has decided that the creature's time has come (at the GM's discretion), or if the creature doesn't wish to return to life, this spell automatically fails, but the cost isn't consumed in the casting.

If the spell is successful, the creature returns to life with 1 Hit Point, no spells prepared or spell slots available, no points in any pools or any other daily resources, and still with any long-term debilitations of the old body. The time spent in the Boneyard leaves the target temporarily debilitated, making it [[Clumsy]] 2, [[Drained]] 2, and [[Enfeebled]] 2 for 1 week; these conditions can't be removed or reduced by any means until the week has passed. The creature is also permanently changed by its time in the afterlife, such as a slight personality shift, a streak of white in the hair, or a strange new birthmark.

**Heightened (7th)** The maximum level of the target increases to 15. The cost increases to the target's level (minimum 1) × 400 gp.

**Heightened (8th)** The maximum level of the target increases to 17. The cost increases to the target's level (minimum 1) × 800 gp.

**Heightened (9th)** The maximum level of the target increases to 19. The cost increases to the target's level (minimum 1) × 1,600 gp.

**Heightened (10th)** The maximum level of the target increases to 21. The cost increases to the target's level (minimum 1) × 3,200 gp.

**Source:** `= this.source` (`= this.source-type`)
