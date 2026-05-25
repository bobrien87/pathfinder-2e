---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Focus]]", "[[Manipulate]]", "[[Sorcerer]]", "[[Void]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 living creature touched"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You instill within a creature the touch of the grave. For the duration, [[Harm]] and [[Heal]] spells treat the creature as undead. In addition, *harm* spells gain a +2 status bonus to the Hit Points restored to the target. An unwilling target can attempt a Will save to reduce the effects.
- **Critical Success** The target is unaffected.
- **Success** The target heals half as much from *heal* and takes half as much damage from *harm* for 1 round.
- **Failure** Effects as described above.

**Heightened (+1)** The status bonus to the Hit Points restored increases by 2.

**Source:** `= this.source` (`= this.source-type`)
