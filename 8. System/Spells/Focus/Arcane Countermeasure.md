---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Focus]]", "[[Manipulate]]", "[[Sorcerer]]"]
cast: "`pf2:r`"
range: "120 feet"
targets: "the spell cast by the triggering creature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** A creature within range that you can see Casts a Spell.

You undermine the target spell, making it easier to defend against. You reduce the spell's rank by 1, and targets of the spell gain a +2 status bonus to any saving throws, skill checks, AC, or DC against it.

You can't reduce the spell's rank below its minimum. For example, a 5th-rank [[Howling Blizzard]] would remain 5th-rank, but a 5th-rank [[Fireball]] would become 4th-rank. Targets still gain all the other benefits, even if you don't reduce the spell's rank.

> [!danger] Effect: Spell Effect: Arcane Countermeasure

**Source:** `= this.source` (`= this.source-type`)
