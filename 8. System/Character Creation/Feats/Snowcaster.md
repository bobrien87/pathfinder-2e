---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Gelid Shard|Gelid Shard]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your magical power grows as the shard's icy influence spreads ever deeper into your being. You gain the basic spellcasting benefits. Each time you gain a spell slot of a new level from this archetype, add a spell of the appropriate spell rank (including heightened versions of lower-rank spells) to your repertoire, either a common spell of the arcane tradition that has the cold trait or another cold spell you have access to.

**Source:** `= this.source` (`= this.source-type`)
