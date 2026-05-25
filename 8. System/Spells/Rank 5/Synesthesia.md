---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The target's senses are suddenly rewired in unexpected ways, causing them to process noises as bursts of color, smells as sounds, and so on. This has three effects, and the target must attempt a Will save.

- Due to the distraction, the target must succeed at a DC 5 flat check each time it uses a concentrate action, or the action fails and is wasted.
- The target's difficulty processing visual input makes all creatures and objects [[Concealed]] from it.
- The creature has trouble moving, making it [[Clumsy]] 3 and giving it a –10-foot status penalty to its Speeds.
- **Critical Success** The target is unaffected.
- **Success** The target is affected for 1 round.
- **Failure** The target is affected for 1 minute.
- **Critical Failure** As failure, and the target is [[Stunned]] 2 as it attempts to process the sensory shifts.

**Heightened (9th)** You can target up to five creatures.

**Source:** `= this.source` (`= this.source-type`)
