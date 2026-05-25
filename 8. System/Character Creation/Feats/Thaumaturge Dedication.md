---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Thaumaturge|Thaumaturge]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Charisma +2"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've uncovered the hidden art of basic thaumaturgy. You become trained in thaumaturge class DC. Choose an implement; you can use it to Glimpse Vulnerability, but don't gain its benefits. You also gain a few esoterica, allowing you to use esoterica actions. You become trained in your choice of Arcana, Nature, Occultism, or Religion; if you were already trained in these, you become trained in a skill of your choice. You gain the [[Glimpse Vulnerability]] action.

Thaumaturge

**Source:** `= this.source` (`= this.source-type`)
