---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]"]
prerequisites: "holy or unholy trait"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your deity's grace doesn't extend to your sworn enemies. When you cast a [[Harm]] or [[Heal]] spell, you can add your holy or unholy trait to it. If you do, the spell deals damage to creatures with the opposing trait, even if it wouldn't normally damage them. The spell deals spirit damage when used this way. For example, if you are holy, you could add the holy trait to a *heal* spell and deal spirit damage to a fiend that has the unholy trait.

**Source:** `= this.source` (`= this.source-type`)
