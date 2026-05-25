---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Unholy]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature that died within the last minute"
duration: "unlimited"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You trap the target's soul in the item before the soul can pass on to the afterlife. The item used to contain the soul can be anything as long as it's of the appropriate value. The item has AC 16 and its normal Hardness and HP. Destroying (not just breaking) an item or counteracting *seize soul* releases the soul to the afterlife.

While the soul is in the item, the target can't be returned to life through any means, even powerful magic such as a [[Wish]] ritual. If the item is destroyed or *seize soul* is counteracted on the item, the soul is freed. An item can't hold more than one soul, and any attempt wastes the spell.

You can also target an item that has had a soul trapped in it with a second casting of *seize soul*, which destroys the item and either releases the soul or relocates it to a different item, whichever you choose. This fails if the target is an artifact or the trapped soul is a creature of 19th level or higher.

**Source:** `= this.source` (`= this.source-type`)
