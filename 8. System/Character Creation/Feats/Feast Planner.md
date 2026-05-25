---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wandering Chef|Wandering Chef]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Wandering Chef Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You learn the [[Fortifying Brew]] ritual, but you instead prepare dishes for a lavish meal that have the same effect as the drinks from the normal version of the ritual. You perform both aspects of the ritual yourself, acting as both primary and a secondary caster. You must still attempt the secondary check normally performed by a secondary caster. In addition, you can use Crafting or Cooking Lore for both the primary and secondary checks. The ritual gains the primal trait as nature spirits attend to you and your guests.

**Source:** `= this.source` (`= this.source-type`)
