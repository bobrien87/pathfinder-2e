---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Merfolk]]", "[[Polymorph]]", "[[Primal]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Using old magic, you slip off your tail like an item of clothing and walk on two feet, resembling a humanoid ancestry, usually human but possibly elf, half-elf, or something stranger. You're still recognizably yourself, as the Shore Gift doesn't change your upper body. While transformed, you lose your swim Speed from your ancestry (though you might still have a swim Speed from other sources) but gain a land Speed of 25 feet.

Using the Shore Gift also counts as creating a disguise when using Deception to Impersonate, and your transformation automatically defeats Perception DCs to determine if you're a normal member of whatever ancestry you appear to be; only creatures actively rolling Perception to examine you might notice the disguise. You can remain in your alternate form indefinitely and can shift back to your merfolk form by using this action again.

**Source:** `= this.source` (`= this.source-type`)
