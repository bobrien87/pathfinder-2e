---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wildspell|Wildspell]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Wildspell Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature Casts a Spell within your [[Spellsurge]] aura.

You cause a surge of magical energy to flare up, harming that creature and those near it. The triggering creature and all creatures adjacent to it take 1d6 untyped damage per rank of the spell ([[Will]] save against your class DC or spell DC, whichever is higher). The damage is of the same type as dealt by the spell (or one type of damage of your choosing if the spell deals multiple types of damage). If the spell doesn't deal damage, the damage is mental. The effect gains the trait of the damage dealt. If you spend a Mythic Point as part of using this reaction, calculate the DC with mythic proficiency; you can also choose to deal acid, cold, electricity, or fire damage instead of the type that would normally be dealt, and creatures that fail the saving throw take persistent damage of the same type as the base effect equal to the rank of the triggering creature's spell.

**Source:** `= this.source` (`= this.source-type`)
