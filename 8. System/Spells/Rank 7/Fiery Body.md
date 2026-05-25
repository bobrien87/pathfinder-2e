---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You become living flame, giving you fire immunity, resistance 10 to precision damage, and weakness 5 to cold and to water. Any creature that touches you or damages you with an unarmed attack or non-reach melee weapon takes 3d6 fire damage.

Your unarmed attacks deal an additional 1d4 fire damage, and your fire spells deal one additional die of fire damage (of the same damage die the spell uses). You can cast [[Ignition]] as an innate spell; the casting is reduced from 2 actions to 1.

In fire form, you have a fly Speed of 40 feet and don't need to breathe.

> [!danger] Effect: Spell Effect: Fiery Body

**Heightened (9th)** Creatures touching you take 4d6 fire damage instead of 3d6, your unarmed attacks deal 2d4 additional fire damage, and you have a fly Speed of 60 feet.

**Source:** `= this.source` (`= this.source-type`)
