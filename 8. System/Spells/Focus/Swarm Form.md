---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "5 minutes"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You discorporate into a swarm of Tiny creatures. While in swarm form, you are the same size, you have the swarm trait and you gain resistance 5 to slashing and piercing damage and weakness 5 to area and splash damage. You can fit into spaces only a few inches wide, moving your constituent creatures through the gap, and you can share a space with another creature. You don't gain the swarm mind ability, so you are still affected normally by mental effects. As a swarm, you can't speak, cast spells, use manipulate actions requiring your hands, activate your magic items, or make any of your Strikes with your normal body. While in swarm form, you can crawl all over any creature that shares your space as a single action. That creature must attempt a Fortitude save against your spell DC or become [[Sickened]] 1 ([[Sickened]] 2 on a critical failure). You can Dismiss the Spell.

**Heightened (+2)** Your resistances and weaknesses each increase by 5.

> [!danger] Effect: Spell Effect: Swarm Form

**Source:** `= this.source` (`= this.source-type`)
