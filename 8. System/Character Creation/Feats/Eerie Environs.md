---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Druid]]", "[[Ranger]]"]
prerequisites: "trained in Intimidation, trained in Stealth"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The natural world can be scary to those not used to it—and you make it scarier still. If you're [[Hidden]] from a creature, you can attempt to `act demoralize` it without losing your hidden condition—imitating the sounds of strange beasts or causing the foliage to rustle menacingly. When you do so, you don't take a penalty to your check if the target doesn't understand your language.

**Source:** `= this.source` (`= this.source-type`)
