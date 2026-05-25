---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Druid]]", "[[Focus]]", "[[Healing]]", "[[Manipulate]]", "[[Plant]]", "[[Vitality]]"]
cast: "`pf2:2`"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Vines twine into a wicker horn in your hands, and out spills a single fruit, nut, or similar small bit of produce. A creature who eats the produce with an Interact action regains 1d6+4 HP. The cornucopia, as well as any unconsumed pieces of fruit, wither away at the end of the duration.

**Heightened (+1)** The cornucopia produces an additional piece of food. A creature can consume any amount of food from the same casting with a single Interact action. Eating six pieces of produce from the cornucopia gives as much nourishment as one square meal for a typical human.

@Damage[((@item.level)d6+(@item.level)*4)[vitality,healing]]{Consume all produce}

**Source:** `= this.source` (`= this.source-type`)
