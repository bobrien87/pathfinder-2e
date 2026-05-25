---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Thlipit Contestant|Thlipit Contestant]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "You have a long prehensile tongue or a tail. At the GM's discretion, similar flexible appendages, such as tentacles, can be used to qualify instead."
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Grueling practice has strengthened your tongue or tail to the point where it's become a formidable weapon. You gain a lash melee unarmed attack that is in the flail weapon group, deals 1d4 bludgeoning damage, and has the grapple and reach traits. The attack can be performed with any appendages you used to qualify for this feat.

Thlipit Contestant

**Source:** `= this.source` (`= this.source-type`)
