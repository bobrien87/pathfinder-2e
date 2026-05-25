---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Swarmkeeper|Swarmkeeper]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Swarmkeeper Dedication"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your swarm takes on characteristics of the death cicadas of the Mana Wastes, whose distinctive buzz is said to be a herald of imminent demise. The inclusion of these death cicadas grants your swarm a fly Speed of 20 feet. You also gain the [[Death Drone]] action.

**Source:** `= this.source` (`= this.source-type`)
