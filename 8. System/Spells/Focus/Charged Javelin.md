---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Cleric]]", "[[Concentrate]]", "[[Electricity]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You fire a javelin of electricity that leaves a charged field around its target. Make a spell attack against the target's AC. The javelin deals 1d6 electricity damage and 1 persistent electricity damage.

As long as the target is taking persistent damage from this spell, creatures gain a +1 status bonus to attack rolls with metal weapons or electricity effects against the target, and the target takes a –1 status penalty to saves against electricity effects.

> [!danger] Effect: Spell Effect: Charged Javelin
- **Critical Success** The javelin deals double damage, both initial and persistent.
- **Success** The javelin deals full damage.

**Heightened (+1)** The initial damage increases by 1d6, and the persistent damage increases by 1.

**Source:** `= this.source` (`= this.source-type`)
