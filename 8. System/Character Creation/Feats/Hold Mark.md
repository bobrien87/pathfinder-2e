---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Orc]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You bear scars or tattoos enhanced by the mark of your community's prowess. When you select this feat, choose one of the options from the below table. You are trained in the listed skill and gain a +1 status bonus to saves against spells from the listed tradition. You gain a large brand or tattoo in the shape of the chosen emblem or a similar concept (for example, the Burning Sun could be a torch, sun, volcano, or other fiery symbol, while the Empty Hand could be a fist or claw).

Hold Mark Emblem
Skill
Tradition

Burning Sun
Diplomacy
Arcane

Death's Head
Survival
Primal

Defiled Corpse
Religion
Divine

Empty Hand
Intimidation
Occult

**Source:** `= this.source` (`= this.source-type`)
