---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

As you challenge an enemy, you take some of its attention away from your allies. The target takes a -1 status penalty to attack rolls, damage rolls, and skill checks against creatures other than you, and you take a -1 status penalty to attack rolls, damage rolls, and skill checks against creatures other than the target.

Each time a creature other than you uses a hostile action that affects the challenged enemy, the enemy can attempt a Will save. On a success, the enemy no longer takes the penalty against that creature. You can Dismiss the spell, and it ends automatically if you or the target is defeated.

**Heightened (+3)** The status penalties increase by 1.

> [!danger] Effect: Spell Effect: Dutiful Challenge

**Source:** `= this.source` (`= this.source-type`)
