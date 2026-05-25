---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Reflection]]", "[[Visual]]"]
frequency: "once per PT1M"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per minute

Due to your origins, your form is more flexible than most. You shift your appearance to resemble a creature within 30 feet but with an unsettling, horrifying twist. Though this transformation is momentary, witnessing it gives the target deep existential dread. It must succeed at a [[Will]] save against the higher of your class DC or spell DC or become [[Frightened]] 1 ([[Frightened]] 2 on a critical failure) and be [[Stupefied 1]] as long as the frightened condition lasts. Once you've used Warped Reflection against a creature, it's temporarily immune for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
