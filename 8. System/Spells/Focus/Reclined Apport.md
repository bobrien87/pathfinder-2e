---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Teleportation]]", "[[Wizard]]"]
cast: "`pf2:1`"
range: "60 feet"
targets: "1 unattended object of light Bulk or less"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Walking over to an item to pick it up is so much effort. Whether it's your spellbook, a reagent, or a glass of wine, it's simply more efficient to call it to your hand. You teleport the target into your open hand. If you don't have a hand free, it falls to the ground at your feet.

**Heightened (3rd)** You can target an unattended object with a Bulk of 1 or less.

**Heightened (5th)** The range increases to 120 feet, and you can target an unattended object with a Bulk of 1 or less.

**Heightened (7th)** The range increases to 120 feet, and you can target an unattended object with a Bulk of 2 or less.

**Source:** `= this.source` (`= this.source-type`)
