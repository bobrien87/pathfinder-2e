---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Amp]]", "[[Occult]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your magic saturates your surroundings with hateful psychic energy. Use this amp in place of a psi cantrip's normal amp entry. The cantrip must be one that takes 2 or more actions to cast and targets a creature.

**Amp** Choose one target of the spell. Psychic phenomena turn themselves on the target-typically, objects fling themselves at the creature. At the beginning of each of the target's turns, it takes 1d4 bludgeoning damage for each spell rank of the psi cantrip this amp was added to, with a [[Reflex]] save. The target remains marked by psychic ire for 3 rounds. The effect persists even if you fall [[Unconscious]] or leave the area.

**Source:** `= this.source` (`= this.source-type`)
