---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Esoterica]]", "[[Thaumaturge]]"]
prerequisites: "mortal weakness or personal antithesis"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're holding an implement and a weapon, you are using Exploit Vulnerability with mortal weakness or personal antithesis, and the target creature is within reach of both your implement and weapon.

As you make an attack augmented by your esoterica, you also press your implement against the creature, applying its weakness as your implement's energies sear the creature's flesh. Make a melee Strike against the target of your Exploit Vulnerability. On any attack roll result but a critical failure, you also press your implement against the creature, automatically dealing the additional damage from Exploit Vulnerability. This is in addition to any damage from your Strike, including the weakness the Strike applies from Exploit Vulnerability. This counts as two attacks when calculating your multiple attack penalty.

**Source:** `= this.source` (`= this.source-type`)
