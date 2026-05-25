---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 item you're holding and 1 item in another creature's possession you can see, each no more than light Bulk"
defense: "Reflex"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You magically swap an item you're holding for another that someone else has. The second item appears in the hand you were holding the first item (or it falls to the ground in your square if you're unable to hold it), and the first item appears in the same place on the other creature's possession where the second item was (held in a hand or attached to a belt, for instance). If the second item is in the possession of a creature unwilling to relinquish it, they can prevent the transposition with a successful Reflex save.

**Heightened (5th)** Each object's maximum Bulk increases to 1. If one of the items is 1 Bulk and the other isn't, an unwilling creature gains a +2 circumstance bonus to their saving throw.

**Source:** `= this.source` (`= this.source-type`)
