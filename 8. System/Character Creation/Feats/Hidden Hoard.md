---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Draconic Acolyte|Draconic Acolyte]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Draconic Acolyte Dedication"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your *draconic gift* is the key to a repository of treasure that only you can access. You create an extradimensional space that can hold up to 100 Bulk worth of objects. The space functions as a spacious pouch, but has no Bulk, and can be Interacted with using only one hand by touching your draconic gift. You can normally store and retrieve items that could fit through the opening of a bag (as spacious pouch). However, you can store an unattended item larger than would normally fit (but no larger than 10 Bulk) by spending 1 minute concentrating on your *draconic gift* as you press it against the object. Retrieving it takes 1 minute and causes the item to appear in the closest unoccupied space.

**Source:** `= this.source` (`= this.source-type`)
