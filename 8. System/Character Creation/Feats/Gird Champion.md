---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Godling|Godling]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Godling Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your will manifests into divine weapons to protect and arm your followers. When you gain this feat, choose one type of weapon with special significance to you, such as a longsword or a sickle. This becomes your favored weapon. You and your hierophant both treat this weapon as a simple weapon for the purposes of proficiency. You and your hierophant gain the critical specialization effect of your favored weapon and deal an additional 1d6 spirit damage with Strikes made with your favored weapon. If one of your current domain spells can deal a type of damage other than spirit, you can choose to match this damage type (for instance, wreathing your weapon in sacred ashes that deal fire damage if you have the fire domain).

> [!danger] Effect: Gird Champion (Hierophant)

**Source:** `= this.source` (`= this.source-type`)
