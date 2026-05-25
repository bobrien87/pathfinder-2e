---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Manipulate]]", "[[Vitality]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 willing living creature"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

An infusion of vital energy grants a creature continuous healing. The target temporarily gains regeneration 15, which restores 15 Hit Points to it at the start of each of its turns. While it has regeneration, the target can't die from taking Hit Point damage and its [[Dying]] condition can't increase to a value that would kill it (this stops most creatures' dying condition at dying 3), though if its [[Wounded]] value becomes 4 or higher, it stays [[Unconscious]] until its wounds are treated. If the target takes acid or fire damage, its regeneration deactivates until after the end of its next turn.

Each time the creature regains Hit Points from regeneration, it also regrows one damaged or ruined organ (if any). During the spell's duration, the creature can also reattach severed body parts by spending an Interact action to hold the body part to the area it was severed from.

> [!danger] Effect: Spell Effect: Regenerate

**Heightened (9th)** The regeneration increases to 20.

**Source:** `= this.source` (`= this.source-type`)
