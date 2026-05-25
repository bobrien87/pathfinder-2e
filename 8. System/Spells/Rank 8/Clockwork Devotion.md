---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "100 feet"
defense: "basic Reflex"
duration: "until the end of your next turn"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You toss a handful of magical cogs before you, summoning a battalion of clockwork soldiers to fight your enemies. The clockwork soldiers occupy the space of a Huge creature and have a Speed of 60 feet.

**Arrive** *Clockwork Assault* Clockwork soldiers slash at your enemies with their halberds, dealing 4d10 slashing damage (basic Reflex save) to all enemy creatures in its location or within 15 feet.

**Depart** (fire) *Ticking Bomb* The clockwork soldiers freeze abruptly before exploding into a mass of flying cogs and metal shrapnel, dealing 4d8 slashing damage and 4d8 fire damage in a 30-foot emanation (basic Reflex save). On a critical failure, a creature takes an additional 2d8 persistent,fire damage.

**Source:** `= this.source` (`= this.source-type`)
