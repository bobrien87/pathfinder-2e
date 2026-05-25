---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Dragonblood]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Visual]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By taking an impressive stance, the full force of your personality cows lesser beings. Each creature in a @Template[emanation|distance:20] must attempt a [[Will]] save against the higher of your class DC or spell DC. Regardless of the result of the saving throw, the creature is temporarily immune to your Majestic Presence for 24 hours.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Frightened]] 1.
- **Failure** The creature is [[Frightened]] 2.
- **Critical Failure** The creature is [[Frightened]] 4.

**Source:** `= this.source` (`= this.source-type`)
