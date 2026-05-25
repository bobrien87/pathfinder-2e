---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Druid]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 Medium or smaller creature"
defense: "Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure an intricate hedge prison to trap a creature, encasing them completely in a hollow cube of dense bushes. The hedge has AC 5, Hardness 5, and 20 Hit Points. It's immune to critical hits and precision damage.
- **Critical Success** The creature escapes the hedge before it fully forms.
- **Success** The creature is trapped inside the hedge, but the hedge's Hit Points are reduced by half.
- **Failure** The creature is trapped inside the hedge.
- **Critical Failure** The creature is trapped inside the hedge, and the hedge's Hit Points are increased by half.

**Heightened (4th)** The hedge's hardness increases to 7 and its Hit Points increase to 30.

**Heightened (5th)** The hedge's hardness increases to 9 and its Hit Points increase to 40. You can target a creature of Large size or smaller.

**Heightened (6th)** The hedge's hardness increases to 11 and its Hit Points increase to 50. You can target a creature of Large size or smaller.

**Heightened (7th)** The hedge's hardness increases to 13 and its Hit Points increase to 60. You can target a creature of Huge size or smaller.

**Heightened (8th)** The hedge's hardness increases to 15 and its Hit Points increase to 70. You can target a creature of Huge size or smaller.

**Heightened (9th)** The hedge's hardness increases to 17 and its Hit Points increase to 80. You can target a creature of Huge size or smaller.

**Source:** `= this.source` (`= this.source-type`)
