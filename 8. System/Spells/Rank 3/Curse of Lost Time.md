---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]", "[[Void]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 Large or smaller object, construct, or living creature"
defense: "Fortitude"
duration: "varies"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You curse the target with rapid aging or erosion. The effect depends on whether the target is an object, a construct, or a living creature. Artifacts, along with objects and constructs made of precious materials (as determined by the GM), are immune.

- **Object** If the object is attended, its bearer can attempt a Fortitude save. If the bearer fails or the object is unattended, the object immediately takes 4d6 damage (applying Hardness normally) and the item is cursed with an unlimited duration. Until the curse ends, the item becomes shoddy and can't be [[Repaired]], and the curse attempts to counteract any spell that would restore the object's Hit Points. [[Cleanse Affliction]] can target an item affected by this spell.

- **Construct** The construct takes 4d6 damage (basic Fortitude save). On a failure, for 1 hour the construct is [[Clumsy]] 1, is [[Enfeebled]] 1, and can't be Repaired, and the curse attempts to counteract any spell that would restore the construct's Hit Points. On a critical failure, these effects have an unlimited duration.

- **Living Creature** The living creature must attempt a Fortitude save. Ageless creatures are immune.
- **Critical Success** The living creature is unaffected.
- **Success** The living creature briefly ages, becoming clumsy 1 and enfeebled 1 for 1 round.
- **Failure** As success, with a duration of 1 hour.
- **Critical Failure** As success, with an unlimited duration.

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
