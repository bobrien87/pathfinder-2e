---
type: feat
source-type: "Remaster"
level: "3"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "trained in Survival"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can find what you're looking for using a dowsing rod or pendulum. If you [[Search]] while wielding a dowsing rod or pendulum, in addition to the normal checks for Searching, the GM rolls a secret Survival check for you to detect the largest source of water, oil, or another natural non-bodily fluid in the area. Even if the liquid is [[Concealed]] from you—for example, if it stems from an underground spring or is piped through a wall—this technique points you in the right direction. The GM determines the DC, which is usually the trained simple DC with a hard or very hard adjustment if the source of water is small.

If you're an expert in Survival, the GM also makes a Survival check for you to detect sizable deposits of metal, minerals, and nearby graves. The DC is usually the expert simple DC, with DC adjustments for smaller deposits.

**Source:** `= this.source` (`= this.source-type`)
