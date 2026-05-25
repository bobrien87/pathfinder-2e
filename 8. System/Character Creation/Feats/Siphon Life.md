---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Aftermath]]", "[[Flourish]]", "[[Magical]]", "[[Void]]"]
prerequisites: "You've been reduced to 0 Hit Points by an enemy with the void trait"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Experiences with necromantic energy have left a permanent mark on you, casting you in a deathlike pallor, chilling your body temperature to be ice-cold, turning your very blood black, and giving you the power to rip out an enemy's life force. Strike with an unarmed attack. If you hit and the target is a living creature, it takes an additional 4d6 void damage, depending on its Fortitude save. If the target takes any void damage, you gain an equal number of temporary Hit Points, which last for 1 minute.
- **Critical Success** The target takes no additional void damage and becomes temporarily immune for 1 minute.
- **Success** The target takes half the additional void damage.
- **Failure** The target takes full additional void damage.
- **Critical Failure** The target takes double the additional void damage.

**Source:** `= this.source` (`= this.source-type`)
