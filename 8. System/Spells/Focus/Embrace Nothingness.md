---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Monk]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You empty your body of substance, becoming one with nothingness. You gain resistance to physical damage equal to your level. You move at half your normal Speed, but can move in any direction (including up and down). While moving, you have concealment. When it is not your turn and during your turn until you take an action with the move trait, you are [[Invisible]]. You can pass through solid inanimate objects as long as they are no more than 2 feet thick

> [!danger] Effect: Spell Effect: Embrace Nothingness

**Source:** `= this.source` (`= this.source-type`)
