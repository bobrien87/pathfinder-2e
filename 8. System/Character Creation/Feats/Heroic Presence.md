---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Emotion]]", "[[Human]]", "[[Mental]]"]
frequency: "once per day"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

The blood of heroes courses through your veins, and you inspire your allies to dig deep and find a new level of resolve. You grant up to 10 willing creatures within 30 feet the effects of a 6th-rank [[Zealous Conviction]], though the effect automatically ends on a target if you give that target a command they would normally find repugnant. This action has the auditory trait or visual trait, depending on how you inspire your allies.

**Source:** `= this.source` (`= this.source-type`)
