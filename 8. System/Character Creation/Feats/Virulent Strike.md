---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Apocalypse Rider|Apocalypse Rider]]"
source-type: "Remaster"
level: "16"
traits: ["[[Flourish]]", "[[Mythic]]"]
prerequisites: "Apocalypse Rider Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Those afflicted by certain maladies are closer to death in your presence. Make a Strike against a creature. If your attack hits, the target must attempt a new saving throw against the highest-level disease or poison that is currently affecting it, possibly progressing it to a higher stage even if the affliction's interval hasn't passed. If the target successfully saves or critically saves against the affliction, the affliction's stage isn't reduced. If your attack was a critical hit, the target takes a –4 circumstance penalty to the save.

> [!danger] Effect: Virulent Strike

**Source:** `= this.source` (`= this.source-type`)
