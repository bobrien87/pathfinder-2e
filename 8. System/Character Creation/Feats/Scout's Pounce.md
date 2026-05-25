---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scout|Scout]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Scout Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are [[Hidden]] from or [[Undetected]] by all of your opponents, and you aren't within 10 feet of any enemy.

You leap from the shadows to strike your foes. Stride up to your Speed, then Strike twice. If you were hidden or unnoticed by the target of these Strikes, your foe is [[Off Guard]] against both attacks.

Your multiple attack penalty applies normally for both attacks.

**Source:** `= this.source` (`= this.source-type`)
