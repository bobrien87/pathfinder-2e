---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Herbalist|Herbalist]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Nature, Natural Medicine"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can create natural remedies. You gain the Advanced Alchemy benefits. You can use advanced alchemy to create 4 alchemical consumables with the healing trait, though the number is reduced by 2 if you didn't make your daily preparations in the wilderness. These consumables are called your herbal items. You remember herbal item formulas and don't need a formula book for them.

You become an expert in Nature and can use Nature instead of Crafting to Craft alchemical consumables with the healing trait. You don't need to be trained in Crafting to do so, and you can use healer's tools instead of alchemist's tools.

Herbalist

**Source:** `= this.source` (`= this.source-type`)
