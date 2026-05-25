---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:r`"
range: "30 feet"
targets: "the triggering creature"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** One of your allies makes a ranged Strike with a weapon with a reload of 1 or less

**Requirements** Your ally has more ammunition for their ranged weapon available.

With a quick gesture, you reload your ally's weapon, allowing them to focus on fighting the enemy. You reload their weapon with a piece of mundane ammunition from the triggering creature's inventory.

**Heightened (4th)** You reload your ally's weapon and grant them a +1 status bonus to their next Strike with this weapon.

> [!danger] Effect: Spell Effect: Helpful Reload

**Heightened (6th)** You reload your ally's weapon with the ammunition of their choice from their inventory. Your ally gains a +1 status bonus to their next Strike with this weapon.

**Heightened (8th)** The spell no longer requires your ally to have appropriate ammunition available. You summon a single piece of common magical ammunition of 10th level or lower to reload your ally's weapon with. Your ally gains a +1 status bonus to their next Strike with this weapon.

**Source:** `= this.source` (`= this.source-type`)
