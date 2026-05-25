---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Leshy]]"]
prerequisites: "chrysanthemum leshy heritage or peachchild leshy heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're adept at hiding your plantlike features to pass as a human. You become trained in Deception (or another skill if you're already trained in Deception). You don't require a disguise kit when attempting Deception checks to Impersonate a human. In addition, you gain a +4 circumstance bonus to Impersonate checks to pretend that you're a human version of yourself, rather than a leshy. This bonus doesn't apply to other checks to Impersonate humans.

**Source:** `= this.source` (`= this.source-type`)
