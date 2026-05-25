---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Illusion]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 living creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A phantasmal image of the most precious thing imaginable to the target appears in a location of your choice within the spell's range. Only the spell's target can see the treasure, though you can see the vague shape of the treasure-be it a pile of items, a deific avatar, or a cherished loved one or hero. The target's response to the treasure is based on the outcome of the target's Will save.
- **Critical Success** The target is unaffected.
- **Success** The target becomes [[Fascinated]] with the treasure, and the duration is until the end of its turn. The target can also try to disbelieve the illusion if it touches the treasure, [[Seeks]] to examine it, or speaks to it if the illusion appears to be a person or the like. If the target disbelieves the illusion, the spell ends.
- **Failure** As success, but the duration is 1 minute.
- **Critical Failure** As success, but the duration is 1 minute. The target finds the treasure so appealing that until the spell ends, it must spend each action focused on it. This can include moving toward the treasure if the target isn't next to it, and [[Interacting]] with the treasure if the target is next to it. (If the illusion appears to be a person or the like, the target can also Interact to converse with it.)

**Source:** `= this.source` (`= this.source-type`)
