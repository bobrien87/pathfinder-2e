---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:2`"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The golden light of a new dawn and the promise of life beyond death radiates from your body. You radiate bright light in a 20-foot radius (and dim light for the next 20 feet) and gain mental resistance 5. Any nindoru fiend or undead that begins its turn adjacent to you must attempt a Will save with the following results.

> [!danger] Effect: Spell Effect: Tomorrow's Dawn
- **Critical Success** The creature is unaffected and immune to this spell's effects for the remainder of the spell's duration.
- **Success** The creature is [[Sickened]] 1 until the end of its turn.
- **Failure** The creature is sickened 1. In addition, it becomes [[Slowed]] 1 until the end of its next turn.
- **Critical Failure** As failure, but [[Sickened]] 2 and the creature remains slowed 1 for the rest of the spell's duration.

**Heightened (6th)** You gain mental resistance 10.

**Heightened (8th)** You gain mental resistance 15.

**Source:** `= this.source` (`= this.source-type`)
