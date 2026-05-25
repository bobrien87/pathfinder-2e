---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Heroic Scion|Heroic Scion]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Heroic Scion Dedication, familiar or nimble or savage animal companion"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're not alone in having a legendary past life—so too does your companion. This previous life might be the return of an animal companion or familiar a previous PC of yours had that perished, or it could be the reincarnation of an entirely different legendary creature. It could even be the returning spirit of a close friend or ally who stood by your side. If you have an animal companion, it gains one specialization of your choice. If you have a familiar, it gains two additional familiar abilities. If your fated companion is slain, you can replace it at no cost when you perform your daily preparations.

**Source:** `= this.source` (`= this.source-type`)
