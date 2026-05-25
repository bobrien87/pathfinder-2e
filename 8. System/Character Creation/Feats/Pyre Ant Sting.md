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

Your swarm's stings burn with agonizing pain, much like that caused by the bright red pyre ants that make their tunnels within the parched sands of deserts like Qadira. Each creature in your swarm's space must succeed at a [[Fortitude]] save against your class DC or spell DC, whichever is higher, or take @Damage[(floor(@actor.level/4))d6[persistent,poison]] damage. A creature that critically fails is also [[Enfeebled]] 1 for as long as it's taking this persistent poison damage.

At 8th level and every 4 levels thereafter, the persistent poison damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
