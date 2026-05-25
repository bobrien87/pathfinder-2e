---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Herbalist|Herbalist]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Herbalist Dedication, trained in Survival"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The herbal items you create use medicinal plants endemic to your location. When a creature consumes one of your herbal items, that creature gains the benefit matching the location where you created that item. If the benefit is not immediate, it lasts for 1 minute unless otherwise stated.

- **Aquatic** Gain a +1 circumstance bonus to Fortitude saves.
- **Arctic** For 1 hour, treat environmental cold effects as if they were one step less severe.
- **Desert** For 1 hour, treat environmental heat effects as if they were one step less severe.
- **Forest** Gain a +2 circumstance bonus to saves against disease and poison effects.
- **Mountain** Gain a +1 circumstance bonus to Reflex saves.
- **Plains** Gain a +1 circumstance bonus to Will saves.
- **Swamp** Remove one source of persistent bleed damage.
- **Underground** Gain a +1 circumstance bonus to Perception.

> [!danger] Effect: Endemic Herbs

**Source:** `= this.source` (`= this.source-type`)
