---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Animist]]", "[[Cleric]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "Embodiment of Balance or Cleric"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Animist** When you channel the powers of life and death, your apparition absorbs and enhances the spiritual energy, carrying it to a nearby ally.

**Cleric** When you pull forth vitality or void energy, you also create a smaller pocket of that energy.

If the next action you use is to cast a 2-action [[Harm]] or [[Heal]] to heal or damage a single creature, choose one additional creature in range. Target that creature with a 1-action version of the same spell. This spell is the same rank as the 2-action *harm* or *heal* you cast and doesn't cost another spell slot.

**Source:** `= this.source` (`= this.source-type`)
