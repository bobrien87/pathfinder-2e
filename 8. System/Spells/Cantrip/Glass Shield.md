---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Earth]]"]
cast: "`pf2:1`"
defense: "basic Reflex"
duration: "until the start of your next turn"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You summon a layer of clear glass to keep you from harm. This counts as using the [[Raise a Shield]] action, giving you a +1 circumstance bonus to AC until the start of your next turn, but it doesn't require a hand to use. You can [[Shield Block]] with the glass shield. It has Hardness 2. You can use the spell's reaction to reduce damage from any spell or magical effect, even if it doesn't deal physical damage. When you Shield Block, the shield explodes in a shower of glass. If creature that broke it is within 5 feet, the shards deal 1d4 piercing damage to that creature with a basic Reflex save. After you use Shield Block, the spell ends and you can't cast it again for 10 minutes.

> [!danger] Effect: Spell Effect: Glass Shield

**Heightened (3rd)** The shield has Hardness 4, and the damage increases to 3d4.

**Heightened (5th)** The shield has Hardness 7, and the damage increases to 4d4.

**Heightened (7th)** The shield has Hardness 10, and the damage increases to 5d4.

**Heightened (9th)** The shield has Hardness 12, and the damage increases to 6d4.

**Source:** `= this.source` (`= this.source-type`)
