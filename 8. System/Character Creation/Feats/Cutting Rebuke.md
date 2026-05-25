---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Mythic]]"]
prerequisites: "Demagogue's Calling or Thespian's Calling"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

If words could kill, the poet might rule the world. Your words can. You gain the [[Bon Mot]] skill feat. You can spend a Mythic Point when rolling the Diplomacy check for Bon Mot to attempt the check at mythic proficiency. If the check succeeds, you can also deal @Damage[(@actor.level)[mental]]{mental damage equal to your level} to the target (double on a critical success).

**Source:** `= this.source` (`= this.source-type`)
