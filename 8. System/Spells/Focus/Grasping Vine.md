---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Plant]]", "[[Wizard]]", "[[Wood]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 unattended object of up to 8 Bulk, or Medium or smaller creature that is currently on the ground"
defense: "Reflex"
duration: "1 minute (see text) (sustained)"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A thick, curling vine erupts from the ground beneath you and stretches to the target, allowing you to move it around. If the target is an item, you can move it 10 feet in any direction within range when you Cast the Spell and the first time you Sustain it each round. If the target is a creature, they must attempt a Reflex save.
- **Critical Success** The target is unaffected and the spell ends.
- **Success** The target is [[Grabbed]] until the end of your next turn unless it Escapes (the vine's [[Escape]] DC is equal to your spell DC) or destroys the vine (the vine has AC 15 and 10 Hit Points), at which point the spell ends.
- **Failure** The target is grabbed until it Escapes or destroys the vine, at which point the spell ends. The first time each round you Sustain this spell, you can [[Reposition]] the grabbed target up to 5 feet.
- **Critical Failure** As failure, and you can immediately Reposition the target up to 10 feet.

**Source:** `= this.source` (`= this.source-type`)
