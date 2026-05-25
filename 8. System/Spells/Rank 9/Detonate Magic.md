---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "5-foot emanation"
targets: "1 magic item or spell effect"
defense: "basic Reflex"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause the magic within the target to dissipate in a destructive explosion. You attempt to counteract the target. If the attempt succeeds, an explosion of magical force deals 8d6 force damage with a basic Reflex save. If you successfully counteract the magic of an item, it's deactivated for 1 week (or destroyed on a critical success) and the explosion is a 5-foot emanation from the item. If you successfully counteract a spell, the effect ends and the explosion affects either all creatures in the spell's area or the target of the spell and all creatures in a 5-foot emanation around it.

**Source:** `= this.source` (`= this.source-type`)
