---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You turn yourself [[Invisible]] and create an illusory duplicate of yourself. When you Sustain the spell, you can mentally dictate a course of action for your duplicate to follow that round. Your duplicate acts as though it had your full number of actions, though it can't actually affect anything in the environment. Both the duplicate and your invisibility persist for the spell's duration. Performing a hostile action doesn't end *mislead*'s invisibility, just like a 4th-rank [[Invisibility]] spell. A creature that determines the duplicate is an illusion doesn't necessarily know you're invisible, and one that can see your invisible form doesn't necessarily know your duplicate is an illusion.

If you Cast a Spell, attack, or otherwise interact with another creature, as a part of that action you can attempt a Deception check against observers' Perception DCs to convince them your duplicate used that action. This doesn't fool anyone who's aware your duplicate is an illusion, nor does it work if the attack obviously couldn't have come from the duplicate. For instance, if you fired a ray, you could make it look like it came from the duplicate as long as the duplicate was positioned appropriately, but if you attacked with a sword and your duplicate was across the room from the target, your Deception check would automatically fail.

**Source:** `= this.source` (`= this.source-type`)
