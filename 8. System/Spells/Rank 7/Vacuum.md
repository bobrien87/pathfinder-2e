---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Air]]", "[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "15-foot emanation"
defense: "Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You inhale all air in the surrounding area, stealing the breath of nearby creatures. During *vacuum*'s duration, you take a –1 circumstance penalty against inhaled threats, such as inhaled poisons. If you cast *vacuum* in an environment where you can't breathe, the spell fails and you immediately begin to suffocate.

Creatures in the area must attempt a Fortitude save. A creature that's holding its breath gets a result one degree of success better than it rolled, and creatures that don't need to breathe air are immune to the spell. A creature that later enters the area or ceases holding its breath must attempt a save against the effect. On subsequent rounds, the first time each round you Sustain the spell, you can force each creature in the area to save against the effect.
- **Success** The creature begins holding its breath.
- **Failure** The creature wheezes and gasps as its breath is stolen, becoming [[Stunned]] 1. The creature then begins holding its breath but has only half its normal number of rounds of remaining air.
- **Critical Failure** The creature has all the air sucked out from its lungs and immediately starts to suffocate.

**Source:** `= this.source` (`= this.source-type`)
