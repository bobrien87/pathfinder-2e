---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Swarmkeeper|Swarmkeeper]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Swarmkeeper Dedication"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your swarm is outside your body.

Your swarm can spin dense webs much like those left by stone-gray weaver spiders under eaves and in derelict city buildings, especially along the coasts of Varisia. When your swarm ends its turn, it fills all surfaces in its space with sticky webs that last for 1 minute. The webs are difficult terrain. A creature that ends its turn in the webs must succeed at a [[Reflex]] save or be [[Immobilized]] until it [[Escapes]]. The webs' save DC and Escape DC are equal to the higher of your class DC or spell DC. The swarm is immune to its webs.

**Source:** `= this.source` (`= this.source-type`)
