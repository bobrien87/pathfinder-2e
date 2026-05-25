---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Beast Lord Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your united companion made a successful Strike against a creature this round.

When you and your companion attack together, you can ensure that escape is but a whispered dream. Strike the same creature that your united companion hit. If your Strike is successful, the targeted creature has been marked for death by you and your companion and can't become [[Hidden]] or [[Concealed]] to you and your companion for 1 minute or until it moves more than 60 feet away from either you or your companion, whichever comes first. If the triggering creature is under an effect or spell that would normally grant it this condition, you can immediately attempt to counteract the effect. Your counteract rank is half your level rounded up, and your counteract check modifier is equal to the higher of your class DC –10 or spell DC –10.

**Source:** `= this.source` (`= this.source-type`)
