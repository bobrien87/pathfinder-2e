---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Monk]]", "[[Stance]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You enter a tight stance, coiled up like a lashing cobra with your hands poised as venomous fangs.

While in this stance, the only Strikes you can make are cobra fang unarmed attacks. These deal 1d4 piercing damage; are in the brawling group; and have the agile, deadly d10, finesse, unarmed, and venomous traits.

While in Cobra Stance, you gain a +1 circumstance bonus to Fortitude saves and your Fortitude DC, and you gain poison resistance equal to half your level.

**Source:** `= this.source` (`= this.source-type`)
