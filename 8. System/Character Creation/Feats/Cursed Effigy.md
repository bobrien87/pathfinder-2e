---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Curse]]", "[[Esoterica]]", "[[Thaumaturge]]"]
prerequisites: "Exploit Vulnerability"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was a successful Strike against the target of your [[Exploit Vulnerability]], and the Strike dealt physical damage.

After your attack, you grab a bit of blood, cut hair, or other piece of the creature's body. You incorporate the material into a premade doll, paper figure, or other effigy to create a sympathetic link that makes it harder to resist your abilities. As long as you are Exploiting Vulnerability against that creature, it takes a –2 status penalty to its saving throws against thaumaturge abilities or items that use your thaumaturge class DC.

**Source:** `= this.source` (`= this.source-type`)
