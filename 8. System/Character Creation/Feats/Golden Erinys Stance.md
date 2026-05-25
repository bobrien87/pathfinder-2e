---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sister Of The Golden Erinys|Sister Of The Golden Erinys]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Stance]]"]
prerequisites: "Sister of the Golden Erinys Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whether you're a keen student of vengeance or you picked up techniques after being a common target for the sisters' punishment, you've learned to dig painfully into your opponent's flesh. In this stance, you can make fury's fang unarmed attacks. These deal 1d6 piercing damage; are in the brawling group; and have the agile, backstabber, finesse, forceful, nonlethal, and unarmed traits.

While in the stance, if you critically hit with a melee Strike that deals piercing damage, the target is [[Sickened]] 1 (with a DC to remove equal to your class DC); this is in addition to any critical specialization effect you might gain from the attack.

**Source:** `= this.source` (`= this.source-type`)
