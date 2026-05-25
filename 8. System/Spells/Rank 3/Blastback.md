---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Air]]", "[[Concentrate]]"]
cast: "`pf2:r`"
area: "20-foot emanation"
defense: "basic Reflex"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You fall more than 10 feet.

You hit the ground with a shuddering boom, propelling the force of your fall out in a wave. You take no damage from the fall as the displaced air allows you to land gently, but all other creatures in the spell's area take 6d4 bludgeoning damage. Creatures that fail their save are also pushed back 5 feet.

**Heightened (+2)** The emanation increases by 10 feet, and the damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
