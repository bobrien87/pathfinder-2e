---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Kobold]]", "[[Magical]]"]
prerequisites: "dragonscaled kobold heritage"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You channel the power of your draconic benefactor to expel a torrent of energy from your mouth that manifests as a @Template[type:line|distance:30] or a @Template[type:cone|distance:15], dealing @Damage[(ceil(@actor.level / 2))d4|options:area-damage] damage. Each creature in the area must attempt a basic saving throw against the higher of your class DC or spell DC. You can't use this ability again for 1d4 rounds.

At 3rd level and every 2 levels after that, the damage increases by 1d4. The breath shape, damage type, and the saving throw match those of your draconic benefactor, such as those shown on the Draconic Benefactors table. This activity has the traits associated with the magical tradition of your draconic benefactor and the type of damage the breath deals.

[[Fortitude]] save [[Reflex]] save [[Will]] save

**Source:** `= this.source` (`= this.source-type`)
