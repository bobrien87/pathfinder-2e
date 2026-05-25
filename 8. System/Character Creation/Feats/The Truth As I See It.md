---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Field Propagandist|Field Propagandist]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Field Propagandist Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your knack for spinning a believable reality from threads of story is so practiced that sometimes even you begin to believe what you're saying. When you use Deception to Lie, you can carefully structure your deceits so that each individual statement you make is the truth, from a certain perspective. Once per day when using Deception to Lie, you can roll twice and take the better result. This is a fortune effect.

You don't take a penalty to Deception checks while subject to the ring of truth spell or similar effects. Whenever you are subject to ring of truth or a similar effect, you can attempt a Deception check when you first begin speaking to counteract the spell's effects, with a counteract rank equal to half your level (rounded up); succeeding at this check doesn't end the spell or effect, but it does cause it to indicate that you are speaking the truth, even when you are actually lying.

> [!danger] Effect: The Truth As I See It

**Source:** `= this.source` (`= this.source-type`)
