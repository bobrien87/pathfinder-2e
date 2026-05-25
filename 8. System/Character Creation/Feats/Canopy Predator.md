---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Verduran Shadow|Verduran Shadow]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Verduran Shadow Dedication, trained in Athletics"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are as at home in the treetops as you are beneath their branches. You gain a climb Speed of 15 feet when moving through trees, vines, and other foliage. Whenever you succeed at an Athletics check to Climb a tree or an Acrobatics check to [[Balance]] on a branch, you get a critical success instead. You aren't [[Off Guard]] while Climbing or Balancing on a tree.

**Source:** `= this.source` (`= this.source-type`)
