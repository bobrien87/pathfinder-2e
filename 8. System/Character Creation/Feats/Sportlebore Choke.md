---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Swarmkeeper|Swarmkeeper]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Swarmkeeper Dedication"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your swarm is outside your body.

Like nefarious sportlebores, a species of insect that plague adventurers by hiding in their rations as counterfeit food, your swarm can crawl down throats. The sportlebores attempt to force their way into the mouth of each creature in your swarm's space. Each creature takes @Damage[(floor(@actor.level/2))d4[piercing]] damage depending on its [[Fortitude]] save against the higher of your class DC or spell DC. The damage increases by 1d4 at 10th level and every 2 levels thereafter. Regardless of the result of its save, the creature is temporarily immune to sportlebore choke for 1 hour.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Sickened]] 1 as it spits out most of the offending sportlebores.
- **Failure** The sportlebores crawl down the creature's throat. The creature takes full damage and is sickened 1.
- **Critical Failure** As failure, but the creature takes double damage and is [[Sickened]] 2.

**Source:** `= this.source` (`= this.source-type`)
