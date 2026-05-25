---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Earth]]", "[[Linguistic]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Fortitude"
duration: "varies"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Many stories tell of a clearing deep in the Mwangi jungle, surrounded by ancient cypress trees. At the center stands an ancient baobab tree growing around a large sphere of black basalt. Legends say that two spirit brothers, Ranage and Golokango, dwelled there long ago until Golokango's evil ways forced the virtuous Ranage to encase his brother in stone. Ranage then transformed himself into a tree to surround and protect the rock for all time. By telling this tale, you condemn an enemy to a stony fate similar to Golokango's and summon plants to surround them.

When you Cast this Spell, every square adjacent to the target becomes difficult terrain from the sudden eruption of plant life for 1 minute. The target also attempts a Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Clumsy]] 1 as their feet are bound within stone. This condition lasts until they move from their current position.
- **Failure** The target is [[Clumsy]] 2 and [[Immobilized]] as their legs are encased in rock. The clumsy condition lasts until they move from their current position, and they can [[Escape]] from being immobilized with a check against your spell DC.
- **Critical Failure** The target is clumsy 2 and [[Restrained]] as nearly their entire body is covered in basalt. The clumsy condition lasts until they move from their current position, and they can Escape from being restrained with a successful check against your spell DC.

**Source:** `= this.source` (`= this.source-type`)
