---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Thaumaturge]]"]
prerequisites: "Exploit Vulnerability, mortal weakness or personal antithesis"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you apply your will to invoke a vulnerability, the result is more powerful, and the vulnerability ripples out in a web from your main target to affect a broader range of creatures. This has one of two effects, based on the type of vulnerability you invoked.

While you have mortal weakness applied, your Strikes also apply that weakness against any creature that has that weakness, not just creatures of the exact same kind. For instance, if you used mortal weakness against a cinder dragon to apply its weakness to cold to your Strikes, those Strikes would also apply to the weakness to cold of fire elementals or any other creature with a weakness to cold.

While you have personal antithesis applied to a non-humanoid creature, you can apply your custom weakness to all creatures of the exact same kind. For example, if you used personal antithesis against an ort, the custom weakness would apply to other orts but not to other types of devils.

**Source:** `= this.source` (`= this.source-type`)
