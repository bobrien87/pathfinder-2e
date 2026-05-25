---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Manipulate]]", "[[Poison]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
defense: "Fortitude"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You turn a creature toward you and exhale a blast of crimson mist from your mouth, exposing the target to a toxic miasma. The effects are determined by the creature's Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target takes 8d6 poison damage.
- **Failure** The target is afflicted with breath of the mantis god poison at stage 1.
- **Critical Failure** The target is afflicted with breath of the mantis god poison at stage 2.

Breath of the Mantis God**Saving Throw** DC 29 [[Fortitude]] save

**Maximum Duration** 6 minutes

**Stage 1** 3d6 persistent bleed and [[Drained]] 1 (1 minute)

**Stage 2** 3d8 persistent bleed and drained 1 (1 minute)

**Stage 3** 3d10 persistent bleed and [[Drained]] 2 (1 minute)

**Source:** `= this.source` (`= this.source-type`)
