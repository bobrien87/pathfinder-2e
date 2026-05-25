---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Fear]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:r`"
range: "30 feet"
targets: "the triggering creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** A creature within range becomes [[Frightened]]

You open your mouth wide and inhale sharply; you draw in the bravery, self-confidence, and hope to which the frightened target clings and then strip away the target's false assumption that these fragile emotions can save them from the oblivion of terror. You deal 6d4 mental damage to the creature, which must attempt a Will saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage; you regain Hit Points equal to half the damage the target takes.
- **Critical Failure** The creature's frightened condition increases by 1 (to a maximum of [[Frightened]] 4) and it takes double damage; you regain Hit Points equal to half the damage the target takes.

**Heightened (+1)** The damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
