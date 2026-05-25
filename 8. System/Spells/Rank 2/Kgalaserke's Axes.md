---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Manipulate]]"]
cast: "1 or 2"
range: "30 feet"
targets: "1 creature"
duration: "1 minute"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The folklore and tales surrounding the legendary hero Kgalaserke are so widespread and well known that a hundred lifetimes would not be enough to have accomplished everything she is reputed to have done. Nevertheless, the stories all contain a unifying theme of her martial prowess despite the odds being stacked against her.

`pf2:1` You briefly describe Kgalaserke's signature axes and how she came to receive them. The target gains a +1 status bonus to attack rolls for the spell's duration.

`pf2:2` You revel in a tale of Kgalaserke striking down a foe after a struggle. For the spell's duration, when the target is damaged by a creature's attack, the target gains a +2 circumstance bonus to damage against that creature for 1 round.

> [!danger] Effect: Spell Effect: Kgalaserke's Axes

**Source:** `= this.source` (`= this.source-type`)
