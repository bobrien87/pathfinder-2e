---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:3`"
range: "100 feet"
duration: "Until you next make your daily preparations"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You craft the illusion of your army being much bigger than it actually is, hoping to overwhelm the opposing forces and shatter their hopes. Your illusion can create up to three illusory Gargantuan duplicates of troops within range. You can give the illusion a basic task to perform, such as standing in formation, marching, mimicking guard movements, or unloading illusory boxes; however, the illusion can't perform any actual tasks and can't create intelligible sounds, such as music or clear speech. If you and any of the illusory troops are ever farther than 500 feet apart, the spell ends.

An illusory troop's AC is equal to your spell DC. Its saving throws modifiers are equal to your spell DC – 10. If an illusory troop is hit by an attack or fails a save, you must attempt a DC 11 flat check. On success, the illusion of that troop is destroyed. On failure, the entire illusion shatters, and all illusory troops are destroyed.

**Heightened (8th)** The DC of the is lowered to 8 (DC 8 flat check), and you can create up to five illusory troops.

**Source:** `= this.source` (`= this.source-type`)
