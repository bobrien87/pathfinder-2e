---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "1 hour"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your body transforms entirely into flexible iron. You gain resistance 10 to physical damage, except adamantine. You're immune to death effects, disease, drained, [[Fatigued]], healing, nonlethal attacks, [[Paralyzed]], poison, sickened, vitality, and void; any of those conditions you had when the spell is cast are suspended until the spell ends, then return with their remaining duration when the spell ends. While made of iron, you're subject to rusting effects like the [[Rust Cloud]] spell.

Your fist Strikes have a 1d10 damage die, and your metal spells deal one additional die of damage (of the same damage die and damage type the spell uses). You can cast [[Needle Darts]] as an innate spell; the casting is reduced from 2 actions to 1.

In this form, you don't need to breathe. Your Bulk doubles (to 6 if you're Small or 12 if you're Medium), and you become too dense to Swim in water, automatically sinking to the bottom. You can Dismiss the spell.

> [!danger] Effect: Spell Effect: Ferrous Form

**Heightened (9th)** The resistance increases to 15.

**Source:** `= this.source` (`= this.source-type`)
