---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Stalwart Defender|Stalwart Defender]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Stalwart Defender Dedication"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You're about to attempt a saving throw against a fear effect.

**Requirements** You're in [[Tenacious Stance]].

As a stalwart defender, you rely on your martial training and your tried-and-true armor to face any danger without flinching. Your mountain-like resilience and courage draw strength from the centuries-old traditions of dwarven song. You bring to mind—and possibly give voice to—a cherished dwarven song of inspiring heroism, granting you a +2 circumstance bonus to the saving throw.

**Source:** `= this.source` (`= this.source-type`)
