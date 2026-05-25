---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Swarmkeeper|Swarmkeeper]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Swarmkeeper Dedication"
frequency: "once per round"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your swarm is outside your body.

Your swarm can emit a bright flash, much like aphet beetles, a genus of flash beetles once used by Osirian miners as sources of light. Each creature in its space must succeed at a [[Fortitude]] save against your class DC or spell DC, whichever is higher, or be [[Dazzled]] for 1 round (2 rounds on a critical failure). The swarm then glows with light like a torch until it returns to your body.

**Source:** `= this.source` (`= this.source-type`)
