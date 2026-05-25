---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Cleric]]"]
prerequisites: "Divine Castigation"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The force of your deity's castigation strengthens your body so you can strike down the enemy and its allies. After you deal spirit damage due to Divine Castigation, your weapon or unarmed Strikes gain your holy or unholy trait and deal additional spirit damage until the end of your turn. The spirit damage is equal to the rank of harm or heal you dealt spirit damage with, and is in addition to any spirit damage the weapon already deals (such as from a holy rune).

**Source:** `= this.source` (`= this.source-type`)
