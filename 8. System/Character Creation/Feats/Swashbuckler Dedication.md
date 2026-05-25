---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Swashbuckler|Swashbuckler]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Charisma +2, Dexterity +2"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Choose a swashbuckler's style. You gain the [[Panache]] and [[Stylish Combatant]] class features, and you apply the bravado trait to [[Tumble Through]] and any actions indicated in your swashbuckler style, allowing you to gain panache. You become trained in Acrobatics or the skill associated with your style. If you were already trained in both skills, you instead become trained in a skill of your choice. You also become trained in swashbuckler class DC. You don't gain any other effects of your chosen style.

Swashbuckler

**Source:** `= this.source` (`= this.source-type`)
