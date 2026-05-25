---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cold]]", "[[Focus]]", "[[Manipulate]]", "[[Oracle]]", "[[Water]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 creature"
defense: "Fortitude"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your touch calls forth a churning mass of icy water that clings to your target, dealing 1d4 bludgeoning damage and 1d4 cold damage. The target must attempt a Fortitude save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage and a –5-foot circumstance penalty to its Speeds until the end of your next turn.
- **Failure** The target takes full damage and a –10-foot circumstance penalty to its Speeds until the end of your next turn.
- **Critical Failure** As failure, but the target takes double damage.

> [!danger] Effect: Spell Effect: Tempest Touch

**Heightened (+1)** The bludgeoning and cold damage each increase by 1d4.

**Source:** `= this.source` (`= this.source-type`)
