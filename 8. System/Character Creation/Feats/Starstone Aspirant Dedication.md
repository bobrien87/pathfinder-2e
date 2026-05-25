---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Starstone Aspirant|Starstone Aspirant]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Divine glory awaits! You embrace your longing to make a true and lasting difference in the Universe by embarking on the path to apotheosis. You dedicate yourself to this journey, striving to overcome all your imperfections. Each day during your daily preparations, choose a skill you're untrained in. You can attempt skill actions that normally require you to be trained in that skill, and you gain a +1 circumstance bonus to checks with that skill until your next daily preparations. At 8th level, this bonus increases to +2, and at 15th level, this bonus increases to +3.

> [!danger] Effect: Starstone Aspirant Dedication

Starstone Aspirant

**Source:** `= this.source` (`= this.source-type`)
