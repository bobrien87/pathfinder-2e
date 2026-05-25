---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Force]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
defense: "Reflex"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause red, ghostly mantis arms to sprout from a nearby surface and crush a creature, dealing 8d6 force damage and attempting to pin the target in place. The effects are determined by the creature's Reflex save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage.
- **Failure** The target takes full damage and is [[Immobilized]] for 1 round.
- **Critical Failure** The target takes double damage and is immobilized for 1 minute. At the end of each of its turns, the target can attempt to [[Escape]]. The Escape DC is equal to your spell DC.

**Heightened (7th)** You can target up to 5 creatures.

**Source:** `= this.source` (`= this.source-type`)
