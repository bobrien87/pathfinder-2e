---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Void]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Fortitude"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A ghostly iron maiden snaps shut on the target and drains its vitality for your gain. This deals 4d4 piercing damage and 4d4 void damage, and the target must attempt a Fortitude save. You gain temporary Hit Points equal to the void damage the target takes (after applying resistances, weaknesses, and the like). You lose any remaining temporary Hit Points after 1 minute.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage.
- **Failure** The target is briefly trapped within the vampiric maiden. The target takes full damage and is [[Immobilized]] by the iron maiden for 1 round or until it uses an Interact action to extricate itself, whichever comes first.
- **Critical Failure** The target takes double damage and is immobilized by the vampiric maiden for 1 round or until it [[Escapes]] (the DC is your spell DC), whichever comes first.

**Heightened (+1)** The piercing and void damage increase by 1d4 each.

**Source:** `= this.source` (`= this.source-type`)
