---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Divine]]", "[[Exemplar]]", "[[Healing]]", "[[Vitality]]"]
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** A living creature within 30 feet would die.

**Requirements** Your divine spark is empowering one of your ikons.

Seeing your ally fall, you let out a cry, sending your divine spark to them temporarily to keep them from tumbling down the River of Souls. You prevent the triggering creature from dying and restore @Damage[5d8[vitality,healing]|shortLabel] Hit Points to them. The ally is invigorated by the touch of your divine power, gaining a +1 status bonus to their saving throws and AC for 1 round.

> [!danger] Effect: Fish From the Falls' Edge

Your divine spark remains with your ally, preventing you from gaining any of your ikons' immanence effects until the start of your next turn, when it returns to an ikon of your choice.

**Source:** `= this.source` (`= this.source-type`)
