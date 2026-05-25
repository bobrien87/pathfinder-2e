---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You craft a 20-foot-tall wall of living flesh in a straight line up to 30 feet long. The wall is 3 feet thick, and each 5-foot-long section has AC 10 and 75 Hit Points. If you wish, the wall can be of a smaller length or height. You must create the wall in an unbroken open space so its edges don't pass through any creatures or objects, or the spell is lost. The wall can't be Repaired but can be healed by vitality, and healing spells and abilities. When you Cast the Spell, choose one of the following features for your wall.

- **Mouths** The wall has countless toothy mouths along its surface. The mouths Strike any creature that ends its turn within 5 feet of the wall, using your spell attack modifier for these Strikes and dealing @Damage[(1+(ceil((@item.level - 4) / 2)))d6[piercing]] damage. The mouths are capable of consuming potions; since the wall is alive, it can recover Hit Points from a Healing Potion, but it can't benefit from any effect that would give it the ability to move. Otherwise, the GM determines which potions can affect the wall.
- **Eyes** The wall sprouts hundreds of unblinking eyes. You can see through these eyes, gaining a +2 circumstance bonus to visual Perception checks within the wall's line of sight. You can also use the eyes for determining line of sight for ranged attacks and spells, but you don't have line of effect through the wall.
- **Arms** The wall is a mass of grasping arms. Any creature that ends its turn within 5 feet of the wall must attempt a Reflex save.
- **Success** The creature is unaffected.
- **Failure** The creature is [[Grabbed]] by the wall for 1 round or until it Escapes against your spell DC, whichever comes first.
- **Critical Failure** The creature is [[Restrained]] by the wall for 1 round or until it Escapes against your spell DC, whichever comes first.

**Heightened (+2)** The Hit Points of each section of the wall increase by 10, and the piercing damage dealt by the wall's mouths increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
