---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Captain|Captain]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "Charisma +2, you don't have an animal companion, construct companion, or other companion that functions similarly"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You become trained in your choice of Diplomacy or Intimidation; if you are already trained in both of these skills, you become trained in a skill of your choice. You also gain your choice of the [[Group Impression]] or the [[Group Coercion]] skill feat. If you already have both of these skill feats, you gain another 1st-level skill feat for which you qualify.

You also gain the assistance of a dedicated follower, who has agreed to accompany you on your journeys. They have the minion trait and begin as a novice follower.

**Special** Once you have a follower, you can never take a feat or class feature that grants an animal companion or another companion that prevents you from having an animal companion.

**Source:** `= this.source` (`= this.source-type`)
