---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Manipulate]]"]
cast: "2 or 3"
range: "40 feet"
targets: "1 creature in line of sight"
defense: "basic Fortitude"
source: "Pathfinder #209: Destroyer's Doom"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cut your own body in a ritualistic manner, causing similar damage to a creature in your line of sight. These cuts are superficial and cause 1d4 slashing damage to you; however, the wounds that open up on our target's body are far deeper. The targeted creature takes 5d8 slashing damage; a creature that critically fails this saving throw also takes @Damage[(1d8 + @item.level -4)[bleed]] damage. If you cast this as a three-action spell, the spell instead affects a 5-foot burst.

**Heightened (+1)** Increase the damage dealt to the target by 1d8, and increase the persistent bleed damage by 1.

**Source:** `= this.source` (`= this.source-type`)
