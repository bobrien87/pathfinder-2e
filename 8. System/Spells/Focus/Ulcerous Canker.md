---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Oracle]]", "[[Poison]]", "[[Void]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 living creature"
defense: "Fortitude"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Weeping sores open on the target as you expose it to decay, dealing 1d4 void damage and 1d4 poison damage plus @Damage[(2*ceil(@item.rank/2)-1)[bleed]] damage. The target must attempt a Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half the initial damage and no persistent bleed damage.
- **Failure** The target takes full damage.
- **Critical Failure** The creature takes double initial damage and double persistent bleed damage.

**Heightened (+2)** The void damage and poison damage each increase by 1d4, and the persistent bleed damage increases by 2.

**Source:** `= this.source` (`= this.source-type`)
