---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
defense: "basic Will"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon the lost and forgotten, assailing your foes' minds with the memories of those who died with a grievance toward them. Enemies in the area take 6d6 mental damage (basic Will save) and are [[Frightened]] 1 on a critical failure.

If you know the names of anyone murdered or grievously wronged by an enemy in the area, you can chant those victims' names when you Cast the Spell to improve the clarity of the visions, increasing the damage to the corresponding enemy from 6d6 to @Damage[(2*(@item.level - 1))d10[mental]|shortLabel]; you can do so for multiple enemies if you know specific victims of each enemy. The visions are personal to each foe in the area, and you can't use this spell to discern a murderer by guessing a name. A creature that truly knows no one who died with any sort of grievance to that creature is immune to this effect.

**Heightened (+1)** The damage increases by 2d6 (or 2d10 to an enemy when you name a specific victim).

**Source:** `= this.source` (`= this.source-type`)
