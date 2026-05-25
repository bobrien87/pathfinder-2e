---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sanguimancer|Sanguimancer]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Sanguimancer Dedication"
source: "Pathfinder #213: Thirst for Blood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Cost** all your remaining sanguimancy Hit Points (minimum 3)

A shell made up of hundreds of razor-thin needles of blood forms around you before exploding outward, lacerating foes in a @Template[type:emanation|distance:30]. The needles deal piercing damage equal to double the number of sanguimancy Hit Points you spent, to a maximum of 80 damage. Creatures caught in the blast must attempt a [[Reflex]] save. The DC for this save is your class DC or spell DC, whichever is higher.

**Source:** `= this.source` (`= this.source-type`)
