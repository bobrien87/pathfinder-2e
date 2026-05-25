---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Godling|Godling]]"
source-type: "Remaster"
level: "16"
traits: ["[[Concentrate]]", "[[Mental]]", "[[Mythic]]"]
prerequisites: "Godling Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your forgiveness is without limit, though the path to penitence can be painful, especially against those who have trespassed against your current mortal form. Spend a Mythic Point; each enemy within a @Template[type:emanation|distance:30] takes @Damage[14d6[mental]|options:area-damage] damage ([[Will]] save against your class DC or spell DC, whichever is higher) as you force them to reflect upon their sins and misdeeds.

Any creature who dealt damage to you or your hierophant since the end of your previous turn uses the outcome one degree of success worse than the result of their saving throw.

> [!danger] Effect: Absolve Sins

**Source:** `= this.source` (`= this.source-type`)
