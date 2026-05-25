---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dragonblood]]", "[[Magical]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Tapping into the physiology of your draconic ancestor, you can exhale a torrent of energy in a @Template[cone|distance:15] or a @Template[line|distance:30], dealing 1d4 damage. Each creature in the area must attempt a basic saving throw against the higher of your class DC or spell DC. You can't use this ability again for 1d4 rounds.

At 3rd level and every 2 levels thereafter, the damage increases by 1d4. The shape of the breath, the damage type, and the saving throw match those of your draconic exemplar. This ability has the trait associated with the type of damage it deals.

**Source:** `= this.source` (`= this.source-type`)
