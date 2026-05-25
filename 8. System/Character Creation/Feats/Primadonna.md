---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Celebrity|Celebrity]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Visual]]"]
prerequisites: "Celebrity Dedication, master in Performance"
frequency: "once per PT1H"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

The spotlight should always be on you and you alone. Attempt a Performance check against the Will DCs of all enemies within @Template[emanation|distance:30]{30 feet} who can see or hear you. On a success, the targets focus on you and gain a +1 circumstance bonus to hit you, but they're [[Off Guard]] to all creatures other than yourself. On a critical success, the effect lasts for 3 rounds.

**Source:** `= this.source` (`= this.source-type`)
