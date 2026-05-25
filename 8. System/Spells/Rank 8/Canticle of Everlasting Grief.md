---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Curse]]", "[[Emotion]]", "[[Fear]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
defense: "basic Will"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a melody distilled from pure grief, conveying the inevitable loss of everything your target cherishes, audible to only them. The target takes 10d6 mental damage depending on its Will save. A creature cursed by this spell can't benefit from circumstance or status bonuses, for the duration noted in the degree of success.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage, is [[Frightened]] 1, and is cursed for 1 round.
- **Failure** The target takes full damage, is [[Frightened]] 3, and is cursed for 1 week.
- **Critical Failure** The target takes double damage, is [[Frightened]] 4, and is cursed for an unlimited duration. While the curse remains, the target's allies are also affected by the curse while within 15 feet of the creature.

**Source:** `= this.source` (`= this.source-type`)
