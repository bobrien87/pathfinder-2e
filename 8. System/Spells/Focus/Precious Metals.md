---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Focus]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 metal shield or weapon, 1 suit of metal armor, or up to 1 Bulk of metal material (such as coins or metal-tipped ammunition)"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your deity blesses base metals to transform them into precious materials. The metal in the target transforms from its normal metal into cold iron, copper, gold, iron, silver, or steel. If the spell's rank is 8th or higher, add adamantine and dawnsilver to the options. If you transform an object into copper, gold, or silver, its Hardness is reduced to 1. Otherwise, its Hardness is increased to 10 if it was lower. An item transmuted in this way deals damage according to its new material. For example, a steel sword transmuted to cold iron would deal additional damage to a creature with a weakness to cold iron. It can have other effects of the new material at the GM's discretion.

This change is clearly magical and temporary, so the item's monetary value doesn't change; you couldn't transmute copper coins to gold and use them to purchase something.

> [!danger] Effect: Spell Effect: Precious Metals

**Heightened (+1)** If you increase the Hardness of the object, the new Hardness is 2 higher.

**Source:** `= this.source` (`= this.source-type`)
