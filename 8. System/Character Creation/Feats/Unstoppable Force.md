---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]"]
prerequisites: "Eternal Legend Dedication, Immovable Object"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

While you are in the stance provided by [[Immovable Object]], you ignore difficult terrain and greater difficult terrain. Once per 10 minutes, if you Dismiss your Immovable Object stance, you can Stride as a free action. At the end of that Stride, your final footfall causes an explosion of energy. Each creature within a @Template[type:emanation|distance:20] takes @Damage[14d6[force]|options:area-damage] damage ([[Reflex]] save against your class DC). Creatures that fail the save are also knocked [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
