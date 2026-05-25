---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Sanctified]]", "[[Spirit]]"]
cast: "`pf2:2`"
range: "100 feet"
targets: "1 creature"
duration: "1 minute"
requirements: "You have a deity."
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

An immense weapon of spiritual energy appears, hovering in the air above the target. The weapon has the ghostly visual appearance of your deity's favored weapon. Name war or peace when you cast this spell.

If you name "war," mentally choose one creature. This must be a creature both you and the target can see. The target instinctively knows which creature this is. At the end of each of the target's turns, if the target didn't use a hostile action against the creature you chose during that turn, the weapon Strikes the target.

If you name "peace," mentally choose up to five allies. The target instinctively knows who those allies are. The weapon Strikes the target each time the target uses a hostile action against you or one of the chosen allies. The weapon Strikes only once per action, even if the action targets multiple allies (such as for a [[Fireball]] or a [[Whirlwind Strike]]).

Strikes with the weapon are melee weapon attacks, but they use your spell attack modifier. Regardless of its appearance, the weapon deals 4d10 damage. The damage type is the same as the chosen weapon (or any of its types for a versatile weapon). The attack deals spirit damage instead if that would be more detrimental to the creature (as determined by the GM). No other statistics or attributes of the weapon apply, and even a ranged weapon attacks adjacent creatures only. The weapon takes a multiple attack penalty, which increases throughout the target's turn, but its penalty is separate from yours.

A weapon of judgment is a weapon for the purposes of triggers, resistances, and so forth. The weapon doesn't take up space, grant flanking, or have any other attributes a creature would. The weapon can't make any attack other than its Strike, and feats or spells that affect weapons don't apply to this weapon.

**Heightened (10th)** The damage increases by 1d10.

**Source:** `= this.source` (`= this.source-type`)
