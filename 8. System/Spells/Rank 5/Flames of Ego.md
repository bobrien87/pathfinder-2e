---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Incapacitation]]", "[[Light]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Elegant flames of incredible beauty coruscate across the target's body, creating overconfidence and carelessness. The target attempts a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target sheds bright light in a @Template[emanation|distance:20] (and dim light to the next 40 feet) and becomes [[Fascinated]] with itself for 1 round. It must spend at least 1 action on its turn on a taunting display of arrogance or overconfidence. Using actions that include such a display—such as using [[Perform]] to show off—count toward this requirement.
- **Failure** As success, but the duration is 1 minute and the target can't act hostile toward a creature until that creature acts hostile toward the target.
- **Critical Failure** As failure, except the target must spend at least 2 actions on its turn on a taunting display of arrogance or overconfidence.

**Source:** `= this.source` (`= this.source-type`)
