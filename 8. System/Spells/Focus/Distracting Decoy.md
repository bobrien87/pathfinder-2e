---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Ranger]]", "[[Visual]]"]
cast: "`pf2:1`"
range: "10 feet"
targets: "1 creature"
defense: "Will"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure a colorful, fast-moving shape, such as a small bird or other animal that draws your target's eye. They must attempt a Will save.
- **Success** The creature is unaffected.
- **Failure** The creature is [[Off Guard]] until the start of your next turn.
- **Critical Failure** As failure, but the creature also takes a –2 circumstance penalty to attacks while it's off-guard.

> [!danger] Effect: Spell Effect: Distracting Decoy

**Source:** `= this.source` (`= this.source-type`)
