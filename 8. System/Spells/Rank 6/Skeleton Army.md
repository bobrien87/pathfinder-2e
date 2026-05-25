---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "100 feet"
duration: "until the end of your next turn"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

With a fistful of compressed bones, you summon a legion of skeletal hulks to fight in your war, refusing to let them rest until they've given up their last inches of usefulness to your cause. The undead army occupies the space of a Huge creature and has a Speed of 40 feet.

**Arrive** *Bone March* The skeletal hulks rise from the dirt, slashing through your enemies and attacking with their dirt-encrusted, bony hands. Enemies within a 20-foot emanation take 4d8 slashing damage (basic Reflex save). On a critical failure, a creature also take 2d8 persistent,bleed damage.

**Depart** *Tossed Heads* Before crumpling into a pile of bones, the skeleton army removes their skulls and throws them at the enemy lines, chattering and howling, dealing 6d6 piercing damage to enemies in a 20-foot burst (basic Reflex save) within 30 feet. On a critical failure, a creature is also [[Frightened]] 2.

**Source:** `= this.source` (`= this.source-type`)
