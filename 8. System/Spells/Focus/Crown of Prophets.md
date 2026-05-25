---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Focus]]", "[[Morph]]"]
cast: "`pf2:1`"
defense: "basic Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Serpents sprout from your head, equally ready to bite your foes or offer you counsel. You gain a fangs unarmed attack that deals 1d6 piercing damage and has the agile, finesse, and versatile poison traits. The first time you Cast or Sustain this spell each round, you can perform one of the following as a free action.

**Serpentine Advice** The snakes compete to offer you counsel. You gain the [[Dubious Knowledge]] feat until the end of your turn, then you [[Recall Knowledge]].

**Toxic Prophecy** (poison)

**Requirements** A creature within 15 feet damaged you since the end of your last turn

**Effect** The snakes spit toxic curses at the required creature, dealing 2d4 poison damage (basic Fortitude save).

> [!danger] Effect: Spell Effect: Crown of Prophets

**Heightened (+1)** The poison damage dealt by Toxic Prophecy increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
