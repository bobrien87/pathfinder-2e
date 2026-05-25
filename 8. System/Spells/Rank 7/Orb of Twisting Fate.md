---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "15 feet"
targets: "1 creature"
defense: "Will"
duration: "up to 1 minute"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The glass orb of an omen dragon erupts from your target's forehead, overwhelming their mind with alternative options.
- **Critical Success** The creature is unaffected.
- **Success** At the start of its turn, the target must decide whether to spend its first action to Stride in a random direction or to spend its first action doing nothing. The spell then ends.
- **Failure** As success, but instead of ending automatically, the target attempts a new save at the end of each of its turns, ending the effect on a success.
- **Critical Failure** As success, but instead of ending automatically, the spell lasts for the full duration.

**Source:** `= this.source` (`= this.source-type`)
