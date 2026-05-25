---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]", "[[Sorcerer]]"]
cast: "1 to 3"
range: "30 feet"
area: "5-foot burst"
defense: "Will"
duration: "1 round"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You sprinkle magical dust in the spell's area, making those within easier to trick. Each creature in the area must attempt a Will save. For each additional action you use when Casting the Spell, increase the burst's radius by 5 feet.
- **Success** The creature is unaffected.
- **Failure** The creature can't use reactions and takes a -2 status penalty to Perception checks and Will saves.

> [!danger] Effect: Spell Effect: Faerie Dust (Failure)
- **Critical Failure** As failure, and the creature also takes a -1 status penalty to Perception checks and Will saves for 1 minute.

> [!danger] Effect: Spell Effect: Faerie Dust (Critical Failure)

**Heightened (+3)** The initial radius increases by 5 feet.

**Source:** `= this.source` (`= this.source-type`)
