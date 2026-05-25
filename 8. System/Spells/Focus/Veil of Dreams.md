---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Focus]]", "[[Hex]]", "[[Manipulate]]", "[[Mental]]", "[[Witch]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your patron draws the target into a drowsy state, causing daydreams and sluggishness. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target takes a -1 status penalty to Perception, attack rolls, and Will saves. This penalty increases to -2 for Will saves against sleep effects.
- **Failure** As success, and any time the target uses a concentrate action, it must succeed at a DC 5 flat check or the action is disrupted.

> [!danger] Effect: Spell Effect: Veil of Dreams

**Source:** `= this.source` (`= this.source-type`)
