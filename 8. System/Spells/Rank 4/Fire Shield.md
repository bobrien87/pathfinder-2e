---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create a hovering shield made of fire. As long as the shield persists, its heat grants you cold resistance 5 and makes you immune to mild and severe environmental cold. You can Raise a Shield with the *fire shield* as a normal shield to gain a +1 circumstance bonus to AC. You can use the Shield Block reaction with the *fire shield*, which has Hardness 10, is immune to fire, and has 40 HP (with no Broken Threshold), and its Hardness is halved against effects that have the water trait. If you Shield Block a melee attack that is either an unarmed attack or made by an adjacent attacker, the attacker takes 2d6 fire damage.

> [!danger] Effect: Spell Effect: Fire Shield

**Heightened (+2)** The cold resistance increases by 5, the HP increase by 10, and the fire damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
