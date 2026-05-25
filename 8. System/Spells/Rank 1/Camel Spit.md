---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Acid]]", "[[Attack]]", "[[Concentrate]]", "[[Manipulate]]", "[[Morph]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You alter your stomach, esophagus, and tongue to be able to spit partially digested food with force. You can spit at a foe once you finish Casting the Spell and can repeat the attack once on each of your subsequent turns by taking a single action, which has the acid, attack, and concentrate traits. After your third spit attack, the spell ends. When you attack with camel spit, make a ranged spell attack roll against a creature within 15 feet, dealing 1d6 acid damage and causing the target to be [[Dazzled]] for 1 round if you hit. On a critical hit, you deal double damage and the target takes @Damage[@item.level[persistent,acid]] damage.

**Heightened (+1)** The damage increases by 1d6, and the persistent damage on a critical hit is increased by 1.

**Source:** `= this.source` (`= this.source-type`)
