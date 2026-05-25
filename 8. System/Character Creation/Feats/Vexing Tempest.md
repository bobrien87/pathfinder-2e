---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Familiar Sage|Familiar Sage]]"
source-type: "Remaster"
level: "12"
traits: ["[[Air]]", "[[Archetype]]", "[[Spellshape]]"]
prerequisites: "Familiar Sage Dedication, Tempest Cloud's Speed"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your familiar channels elemental air around it to unleash a disruptive gust that sends creatures flying. If the next action you use is to Cast a Spell that has the air trait, all creatures within a @Template[type:emanation|distance:15] of your familiar must attempt a Reflex save against your spell DC or be pushed 10 feet away. On a critical failure, they're also knocked [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
