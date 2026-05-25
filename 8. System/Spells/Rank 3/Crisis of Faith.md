---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You assault the target's faith, riddling the creature with doubt and mental turmoil that deal 6d6 mental damage, or 6d8 mental damage if it can cast divine spells. The effects are determined by its Will save.

To many deities, casting this spell on a follower of your own deity without significant cause is anathema.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage.
- **Failure** The target takes full damage; if the target can cast divine spells, it's [[Stupefied 1]] for 1 round.
- **Critical Failure** The target takes double damage, is [[Stupefied 1]] for 1 round, and can't cast divine spells for 1 round.

**Heightened (+1)** The damage increases by 2d6 (or by 2d8 if the target is a divine spellcaster).

**Source:** `= this.source` (`= this.source-type`)
