---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Monk]]", "[[Stance]]"]
prerequisites: "trained in Deception"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're unarmored.

Your body moves like a petal twisting on the wind, confounding your opponents while using their energy against them. You can make gale blossom strikes that deal 1d6 slashing damage. These strikes are in the brawling group and have the agile, finesse, nonlethal, shove, and unarmed traits. While in Twisting Petal Stance, you gain a +1 circumstance bonus to Athletics checks to [[Shove]] and a +2 circumstance bonus to your Fortitude DC to avoid being Shoved. You also gain a +1 circumstance bonus to Deception checks to [[Feint]] and a +2 circumstance bonus to your Perception DC to resist an opponent's Feint attempt.

**Source:** `= this.source` (`= this.source-type`)
