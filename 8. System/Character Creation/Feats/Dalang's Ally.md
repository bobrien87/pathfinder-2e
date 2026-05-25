---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Occult]]", "[[Shadow]]", "[[Wayang]]"]
frequency: "once per PT1H"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You move your shadow as a master puppeteer, allowing it to dance around your enemies and serve you in combat. Until the start of your next turn, your shadow darts around with your foes, providing flanking for you against all enemies within your reach. Flanking with your shadow is the same as flanking with an ally and so is subject to effects like all-around vision or the deny advantage class feature.

**Source:** `= this.source` (`= this.source-type`)
