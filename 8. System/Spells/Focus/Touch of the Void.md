---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Champion]]", "[[Focus]]", "[[Manipulate]]", "[[Void]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 willing undead creature or 1 living creature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You infuse the target with void energy, healing undead or damaging a living creature.

- **Willing Undead Creature** The target regains 6 Hit Points. If the target is yourself, you also gain a +2 status bonus to damage rolls for 1 round.
- **Living Creature** The target takes 1d6 void damage with a basic Fortitude save; on a failure, the target also takes a –2 status penalty to AC for 1 round.

> [!danger] Effect: Spell Effect: Touch of the Void

**Heightened (+1)** The amount of healing increases by 6, and the damage to a living target increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
