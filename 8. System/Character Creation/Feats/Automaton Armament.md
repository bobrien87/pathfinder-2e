---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Automaton]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've been provided a body part designed for combat. You gain either a claw or pincer unarmed attack. The claw deals 1d4 slashing damage, is in the brawling group, and has the agile, finesse, and unarmed traits. The pincer deals 1d6 piercing damage, is in the brawling group, and has the grapple and unarmed traits. Your body can be reconfigured; you can select this feat at any level, and you can retrain into or out of this feat or change the type of attack you gain.

**Enhancement** Your attacking part is reinforced. Increase the damage die of the unarmed attack you gain from this feat by one step (from 1d4 to 1d6, or from 1d6 to 1d8).

**Source:** `= this.source` (`= this.source-type`)
