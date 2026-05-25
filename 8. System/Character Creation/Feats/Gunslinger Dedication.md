---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Gunslinger|Gunslinger]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Dexterity +2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You excel in using specific types of ranged weapons. You have familiarity with martial crossbows and firearms, treating them as simple weapons for the purposes of proficiency.

You gain access to uncommon martial and simple crossbows and firearms that do not have an ancestry trait. You become trained in gunslinger class DC.

Choose a gunslinger way. You become trained in your way's associated skill; if you were already trained in this skill, you become trained in a skill of your choice. You don't gain any other abilities from your choice of way.

Gunslinger

**Source:** `= this.source` (`= this.source-type`)
