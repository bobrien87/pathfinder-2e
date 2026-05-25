---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Necrologist|Necrologist]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Flourish]]", "[[Manipulate]]", "[[Visual]]"]
prerequisites: "Necrologist Dedication"
frequency: "once per PT10M"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

**Requirements** Your horde is raised.

Your horde can drag unwilling victims along with it as it shambles forward. Your horde Strides up to its Speed and can move through the spaces of Large and smaller creatures, but it must end its movement in an unoccupied space. Each creature whose space it moves through is subjected to the horde's [[Mobbing Assault]], attempting a basic Reflex save as usual. A creature who fails the saving throw is also [[Repositioned]] to an unoccupied square of your choice adjacent to the horde's final position. You can't move the creature into or through obstacles.

**Source:** `= this.source` (`= this.source-type`)
