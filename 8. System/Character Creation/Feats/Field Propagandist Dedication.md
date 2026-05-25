---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Field Propagandist|Field Propagandist]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "Charisma +2, trained in Deception and Diplomacy"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Having devoted your life to crafting propaganda, you know that winning the hearts and minds of soldiers can be a deciding factor in securing the successful outcome of a war. You gain the [[Spread Propaganda]] exploration activity.

While you are not immune to propaganda, you are resistant to it. You gain a +2 circumstance bonus to your Perception DC against attempts made by others to Lie to you. If you have the Lie to Me skill feat, you gain a +2 circumstance bonus to your Deception DC.

You become trained in Society. If you were already trained, you become an expert instead.

Field Propagandist

**Source:** `= this.source` (`= this.source-type`)
