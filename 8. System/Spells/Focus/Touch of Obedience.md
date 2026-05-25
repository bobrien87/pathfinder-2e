---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 living creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your imperious touch erodes the target's willpower, making it easier to control. The target attempts a Will save. Regardless of the result, it's then temporarily immune for 1 hour.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Stupefied 1]] until the end of your next turn.
- **Failure** The target is [[Stupefied 2]] until the end of your next turn.
- **Critical Failure** The target is [[Stupefied 2]] for 1 minute and is forced to its knees, becoming prone.

**Source:** `= this.source` (`= this.source-type`)
