---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wandering Chef|Wandering Chef]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]"]
prerequisites: "Morning Side Dishes"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can create dishes that reflect the food sources endemic to your environment and medicinal food techniques utilizing the cycle of the five elements. When you create alchemical food from Morning Side Dishes during your daily preparations, you can add one elemental benefit of your choice to each of the items. This benefit comes in addition to any other effect of consuming the item. Each element has an immediate benefit and a +3 item bonus to certain saves that lasts for 1 hour after the food is consumed. The item bonus increases to +4 if the alchemical item is 18th level or higher.

- **Wood** Remove one source of persistent bleed. For 1 hour, gain a +3 item bonus to saves against disease and poison effects.
- **Fire** Reduce the [[Clumsy]] condition by 1. For 1 hour, gain a +3 item bonus to saves against being [[Doomed]] or [[Frightened]].
- **Earth** Reduce the [[Drained]] condition by 1. For 1 hour, gain a +3 item bonus to saves against being [[Enfeebled]].
- **Metal** Reduce the [[Stupefied]] condition by 1. For 1 hour, gain a +3 item bonus to saves against being stupefied.
- **Water** Reduce the frightened condition by 2. For 1 hour, gain a +3 item bonus to saves against [[Deafened]] or drained.

> [!danger] Effect: Regional Specialty

**Source:** `= this.source` (`= this.source-type`)
