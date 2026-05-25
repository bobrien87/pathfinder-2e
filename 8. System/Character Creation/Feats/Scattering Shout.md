---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Eternal Legend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a flex of your mighty thews and a guttural bellow that can make ears bleed, you drive back any enemies surrounding you. Each enemy within a @Template[type:emanation|distance:10] must attempt a [[Fortitude]] save saving throw against your class DC.
- **Critical Success** The creature is unaffected.
- **Success** The creature is pushed 5 feet away from you.
- **Failure** The creature is pushed 10 feet away from you and takes @Damage[8d6[sonic]|options:area-damage] damage.
- **Critical Failure** The creature is pushed 15 feet away from you and takes @Damage[16d6[sonic]|options:area-damage] damage.

**Source:** `= this.source` (`= this.source-type`)
