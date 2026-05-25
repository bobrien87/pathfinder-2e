---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Auditory]]", "[[Barbarian]]", "[[Rage]]", "[[Visual]]"]
prerequisites: "Share Rage"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can drive your allies into a frenzy, granting them incredible benefits. You can ignore the requirements of Share Rage, using it multiple times in a Rage. Allies affected by [[Share Rage]] can choose to gain your instinct ability and the specialization ability it gains from weapon specialization, but not greater weapon specialization. They must abide by any restrictions of your instinct if they do so (such as the anathema of the superstition instinct).

**Source:** `= this.source` (`= this.source-type`)
