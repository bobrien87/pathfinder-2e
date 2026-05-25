---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Exemplar]]", "[[Polymorph]]"]
prerequisites: "plunderer of the hive's riches"
frequency: "once per PT1H"
source: "Pathfinder #217: Death Sails a Wine-Dark Sea"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

Though you may have stolen from the hive, you've nothing but respect for the armies guarding it, and you borrow their strength to overwhelm your foes. Your body transforms into a swarm of bees. You Fly up to twice your Speed; during this movement you can pass through any space that would be small enough for a single insect, and your movement does not trigger reactions. If you pass through an enemy's space, you can inflict a storm of stings that deals @Damage[(floor((@actor.level - 2)/ 2)d4)[piercing],(floor((@actor.level - 2)/ 2)d4)[poison]] damage, with a [[Reflex]] save against your class DC. At the end of your movement, you return to your original form. At 10th level and every two levels thereafter, the damage increases by 1d4 piercing damage and 1d4 poison damage.

**Source:** `= this.source` (`= this.source-type`)
