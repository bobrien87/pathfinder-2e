---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Lizardfolk]]"]
prerequisites: "bakuwa lizardfolk heritage or Tian Xia origin"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A hump forms on your back that allows you to attack and trap spirits. Your weapon and unarmed attack Strikes against incorporeal creatures become magical. If they're already magical, they instead gain the effects of a [[Ghost Touch]] rune.

**Special** If you have access to this feat but aren't a bakuwa lizardfolk, your body doesn't change when you take this feat. You must instead wear a physical coffin, which is a small wooden chest of light Bulk that you specially anoint during your daily preparations. If your chest is missing or destroyed, you lose the benefits of spirit coffin until you've replaced and re-anointed it.

**Source:** `= this.source` (`= this.source-type`)
