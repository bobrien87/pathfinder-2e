---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ostilli Host|Ostilli Host]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Healing]]"]
prerequisites: "Ostilli Host Dedication"
frequency: "once per day"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your ostilli takes control of your nervous system and kicks your cellular functions into overdrive when you're about to die. You regain Hit Points equal to your level. For the next 2 rounds, at the start of your turn, you regain Hit Points equal to half your level. The first time you regain Hit Points at the start of your turn, you reduce your wounded condition by 1.

**Source:** `= this.source` (`= this.source-type`)
