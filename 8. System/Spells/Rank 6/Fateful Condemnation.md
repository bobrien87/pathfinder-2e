---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Aura]]", "[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 living creature"
defense: "Will"
duration: "1 minute"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You draw upon the target's negative fate, causing this lingering destiny to afflict it and its nearby allies with the unintended consequences of its past lives. Spiritual echoes of the target's past lives instill overwhelming feelings of doubt, regret, and despair into the minds of the target and its nearby allies. The effects depend on the target's Will save, with the following results.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes 4d6 mental damage, and then an aura of shimmering mist with a @Template[emanation|distance:10] surrounds the creature. This mist isn't dense enough to affect sight, but it does cause the creature and any of its allies in the aura to take a –1 status penalty to all skill checks.
- **Failure** As success, but the creature takes an initial 8d6 mental damage and is then [[Slowed]] 1 for the duration of the effect.
- **Critical Failure** As success, but the creature takes an initial 16d6 mental damage, then is slowed 1 for the duration of the effect. Any of the target's allies who begin their turn in the @Template[emanation|distance:10] is slowed 1 for 1 round.

**Source:** `= this.source` (`= this.source-type`)
