---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Sorcerer]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
duration: "varies"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a vicious barbed spear and hurl it at a foe. Make a ranged spell attack roll, dealing 1d8 piercing damage on a success and double damage on a critical success. The spear remains lodged within a creature it hits, making the target [[Clumsy]] 1 (or increasing its clumsy condition by 1 if it is already clumsy) for 1 minute or until the spear is removed with a successful Athletics check against your spell DC as an Interact action, whichever comes first.

**Heightened (+1)** The initial damage increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
