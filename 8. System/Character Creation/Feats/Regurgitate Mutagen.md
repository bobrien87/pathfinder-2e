---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Alchemist]]", "[[Manipulate]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are under the effects of a mutagen.

You redirect a mutagen within your body to spit a stream of stomach acid at a foe. A creature within 30 feet takes 1d6 acid damage for every 2 levels you have (@Damage[(floor(@actor.level/2))d6[acid]]), with a [[Reflex]] save against your class DC. On a failure, the creature is also [[Sickened]] 1 (or [[Sickened]] 2 on a critical failure). The mutagen's duration immediately ends.

**Source:** `= this.source` (`= this.source-type`)
