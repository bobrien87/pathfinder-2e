---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Manipulate]]", "[[Morph]]"]
cast: "`pf2:2`"
range: "10 feet"
targets: "1 creature"
requirements: "You're mostly or totally submerged in water."
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Requirements** You're mostly or totally submerged in water.

You temporarily shape your lower limbs into the tail of a hippocampus in order to swim away from a nearby foe after dealing a parting blow. Attempt a melee spell attack roll against the target's AC, dealing 2d6 bludgeoning damage on a hit (or double damage on a critical hit). Then, Swim up to 30 feet; if you already have a swim Speed, you can Swim up to your Speed with a +10-foot circumstance bonus. You gain a +2 circumstance bonus to your AC against reactions triggered by this movement. At the end of the movement, your lower limbs return to normal.

> [!danger] Effect: Spell Effect: Hippocampus Retreat

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
