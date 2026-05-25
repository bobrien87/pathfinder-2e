---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Apocalypse Rider|Apocalypse Rider]]"
source-type: "Remaster"
level: "18"
traits: ["[[Manipulate]]", "[[Mental]]", "[[Mythic]]"]
prerequisites: "Apocalypse Rider Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a look and a gesture, you turn a thinking creature's mind against itself, causing the creature to struggle to remember how to perform more complex actions. Choose a target within 30 feet and spend a Mythic Point. The target must attempt a [[Will]] save against your class DC or spell DC (whichever is higher) at mythic proficiency.
- **Critical Success** The target is unaffected.
- **Success** For the next 3 rounds, if the target performs an activity that requires three or more actions, they take 12d8 mental damage.
- **Failure** For the next 3 rounds, if the target performs an activity that requires two or more actions, they take 12d8 mental damage.
- **Critical Failure** As failure, but the target is also [[Stunned]] 1 as its mind struggles to function.

**Source:** `= this.source` (`= this.source-type`)
