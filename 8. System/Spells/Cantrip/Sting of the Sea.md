---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Hex]]", "[[Witch]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 creature"
defense: "Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A long tentacle like that belonging to an octopus, anemone, or man-of-war, dripping with briny water, appears from a glowing blue portal to wrap around the target's face, blocking its vision. For the duration of the spell, the target must attempt a Fortitude save at the beginning of its turn. The portal follows the target around, and the tentacle can't be targeted or harmed.
- **Critical Success** The target is unaffected.
- **Success** The target takes a –2 penalty to Perception checks involving vision until the end of its turn. 

> [!danger] Effect: Spell Effect: Sting of the Sea
- **Failure** The target is [[Dazzled]] until the end of its turn.
- **Critical Failure** The target is [[Blinded]] until the end of its turn.

**Source:** `= this.source` (`= this.source-type`)
