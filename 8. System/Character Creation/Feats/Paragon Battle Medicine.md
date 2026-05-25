---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "Battle Medicine, master in Medicine"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You’re from Rahadoum.

Kassi Aziril taught you her techniques that originated the modern use of Battle Medicine. When you successfully use Battle Medicine, you can also reduce the target's [[Sickened]], [[Enfeebled]], or [[Clumsy]] condition by 1 (this has no effect if you are subject to an effect continually applying the clumsy condition, like enlarge).

If you are legendary in Medicine, you can choose to reduce the target's [[Frightened]] or [[Stunned]] condition by 1 instead, and if you have the [[Godless Healing]] feat, you can choose to reduce the target's [[Stupefied]] or [[Drained]] condition by 1 instead.

If you have the [[Mortal Healing]] feat, you can reduce all available conditions by 1 for a target who hasn't benefited from vitality or healing magic in the last 24 hours, and if you roll a critical success before applying the effects of the feat, you reduce all available conditions by 2 for that target instead.

**Source:** `= this.source` (`= this.source-type`)
