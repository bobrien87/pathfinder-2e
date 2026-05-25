---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "500 feet"
defense: "basic Reflex"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 4 40-foot bursts

You reach into the skies and call down an array of falling stars that explode upon colliding with the ground. Choose for the falling stars to be airbursts (sonic), asteroids (fire), comets (cold), or plasma (electricity). The spell gains the trait of the falling star type you chose. The four stars' central 10-foot bursts can't overlap. Each falling star deals 6d10 bludgeoning damage to each creature in the @Template[burst|distance:10] at the center of its area of effect before exploding, dealing 14d6 energy damage of the type you chose to each creature in its @Template[burst|distance:40]. A creature in any of the areas attempts one basic Reflex save against the spell no matter how many overlapping explosions it's caught in and can take each type of damage only once.

**Heightened (+1)** The bludgeoning damage increases by 1d10, and the energy damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
