---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Godling|Godling]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Godling Dedication, hero-god accomplishment"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your myth speaks of distant travel to countless countries, planes, or dimensions. When any effect attempts to anchor you to a plane (such as [[Planar Tether]]) or to banish you from the current plane (such as [[Banishment]]), that effect gains the incapacitation trait. If it already has the incapacitation trait, you gain a +4 status bonus to your save against the effect. If you successfully save against such an effect, the creature that attempted to use this effect on you must succeed at a [[Will]] save against your class or spell DC (whichever is higher) to avoid becoming [[Stupefied 1]] for 1 minute ([[Stupefied 2]] on a critical failure).

You also lay claim to one of the following domains of your choice: dreams, fate, or travel.

**Source:** `= this.source` (`= this.source-type`)
