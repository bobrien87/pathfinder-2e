---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Gelid Shard|Gelid Shard]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your attunement to arcane cold enhances the depths of your growing power. Increase the number of spells in your repertoire and number of spell slots you gain from *gelid shard* archetype feats by 1 for each spell rank other than your two highest *gelid shard* spell slots.

**Source:** `= this.source` (`= this.source-type`)
