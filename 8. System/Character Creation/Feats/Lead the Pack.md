---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beastmaster|Beastmaster]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Mature Beastmaster Companion, you have multiple animal companions"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can have up to two animal companions active at once. However, when you do, it's slightly more difficult to [[Command]] them. If you don't Command either of your companions, one of the two (your choice) can still use 1 action on your turn to Stride or Strike, as per Mature Beastmaster Companion, but not both.

When you Command an Animal, either choose one of the companions to take 2 actions, as normal, or else both companions can take 1 action to Stride or Strike. Either way, you can't Command an Animal to make either companion act again until your next turn.

**Source:** `= this.source` (`= this.source-type`)
