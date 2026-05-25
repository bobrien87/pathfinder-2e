---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ascended Celestial|Ascended Celestial]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]"]
prerequisites: "Ascended Celestial Dedication, Channel Divine Spark"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you unleash your divine spark, you become a being of living light that scours away the darkness. While Channeling your Divine Spark, you become immune to the [[Confused]] and [[Frightened]] conditions. Any creature that touches you or damages you with an unarmed melee attack or a non-reach melee weapon takes 3d6 fire damage, your unarmed attacks deal 1d6 additional fire damage, and your fire spells deal one additional die of fire damage (of the same damage die the spell uses). This damage is doubled against creatures with the aberration, fiend, or undead trait.

**Source:** `= this.source` (`= this.source-type`)
