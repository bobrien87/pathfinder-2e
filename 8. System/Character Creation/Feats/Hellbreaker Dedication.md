---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellbreaker|Hellbreaker]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're a member of the Hellbreakers league.

By joining the League, you've taken on the responsibilities of a Hellbreaker. You gain the [[Additional Lore]] general feat for both Devil Lore and Hellknight Lore. If you were already trained in one or both of those Lore skills, you also become trained in a Lore skill of your choice.

When you roll initiative, you can attempt a `act recall-knowledge skill=devil-lore`, `act recall-knowledge skill=hellknight-lore`, or `act recall-knowledge skill=society` check to [[Recall Knowledge]] about one enemy you can see as a free action, if that skill would be applicable. The GM is the final arbiter of whether or not one of those skills would be appropriate to Recall Knowledge about the enemy.

**Source:** `= this.source` (`= this.source-type`)
