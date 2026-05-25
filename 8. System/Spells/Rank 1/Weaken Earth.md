---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature, unattended object, or hazard or structure made of stone or earth"
defense: "Fortitude"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You weaken the bonds that hold earth and stone together. If your target has Hardness, you can affect one contiguous object, up to a 5-foot cube, or one creature, decreasing the Hardness by 5, to a minimum of 0. If the target lacks Hardness, it gains weakness 3 to physical damage. A target with a Fortitude modifier can attempt a Fortitude saving throw, negating the effect on a success.

> [!danger] Effect: Spell Effect: Weaken Earth

**Heightened (+2)** Hardness decreases by 5, the size of a contiguous object increases by one 5-foot cube, and the weakness increases by 3.

**Source:** `= this.source` (`= this.source-type`)
