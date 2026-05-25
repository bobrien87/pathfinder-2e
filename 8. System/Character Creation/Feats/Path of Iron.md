---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Martial Artist|Martial Artist]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Martial Artist Dedication"
frequency: "once per PT1M"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

With a burst of effort and speed, you weave a nimble path through your many enemies, striking each in turn as you move past them. You Stride; this movement doesn't trigger reactions. You can attempt a melee Strike up to three times at any point during your movement, each against a different enemy. Each attack counts toward your multiple attack penalty, but your multiple attack penalty doesn't increase until you have made all your attacks.

**Source:** `= this.source` (`= this.source-type`)
