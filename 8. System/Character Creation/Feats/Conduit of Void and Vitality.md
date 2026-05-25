---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Oracle]]"]
prerequisites: "any oracle mystery"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have [[Heal]] or [[Harm]] as a signature spell and an available spell slot to cast it with.

You use the unstable energy of your curse to manipulate the most basic of divine magic. You cast a 3-action *heal* or *harm* spell, expending the slot as normal. If the spell restores Hit Points to one or more creatures, then one creature healed by this spell regains a number of additional Hit Points equal to 1d8 × your [[Cursebound]] value; if the spell damages one or more creatures, then one creature harmed by this spell takes additional damage equal to 1d8 × your cursebound value.

**Source:** `= this.source` (`= this.source-type`)
