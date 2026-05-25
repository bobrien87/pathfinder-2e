---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Void]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature or object"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your touch rots organic material and decays objects. Make a spell attack against the target's AC. Your touch deals 1d12 void damage plus 1d4 persistent void damage. If a creature uses an item to block withering grasp, such as with the Shield Block reaction, the item is automatically affected, but the creature doesn't take damage (even if there is damage left over after the shield's Hardness). Unlike normal void damage, the void damage from withering grasp damages objects, constructs, and the like by eroding away their substance.
- **Critical Success** Your touch deals double damage (both initial and persistent). If you target an object, lower its Hardness by 4 for 1 minute.
- **Success** Your touch deals full damage. If you target an object, lower its Hardness by 2 for 1 minute.

**Heightened (+1)** The damage increases by 1d12 and the persistent damage increases by 1. If you target an object, lower its Hardness by an additional 1 point on both a success and a critical success.

**Source:** `= this.source` (`= this.source-type`)
