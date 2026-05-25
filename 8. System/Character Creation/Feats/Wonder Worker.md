---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Thaumaturge]]"]
prerequisites: "legendary in Arcana, Nature, Occultism, or Religion"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The thaumaturge's path culminates with the working of wonders. Once per day, you can align your esoterica to cast a spell of 8th rank or lower that takes 1, 2, or 3 actions to cast. The spell must be common or one to which you have access. You can choose a spell of any tradition for which you're legendary in the associated skill (Arcana for arcane, Nature for primal, Occultism for occult, or Religion for divine). Use your thaumaturge class DC in place of any necessary spell DC and your thaumaturge class DC - 10 in place of any necessary counteract modifier or spell attack modifier.

**Source:** `= this.source` (`= this.source-type`)
