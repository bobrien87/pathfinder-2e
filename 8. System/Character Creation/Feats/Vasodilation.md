---
type: feat
source-type: "Remaster"
level: "2"
prerequisites: "trained in Medicine"
source: "Pathfinder #213: Thirst for Blood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Using the power of your own blood, you encourage increased blood flow to nourish damaged tissue or stifle the flow to clot wounds or prevent the spread of poison and disease. You no longer require a healer's toolkit to [[Administer First Aid]], [[Treat Disease]], [[Treat Poison]], or [[Treat Wounds]], though you take 1 untyped damage each time you take one of these actions without the proper tools from the expenditure of your blood. You can't reduce or prevent this damage.

You gain a +1 item bonus when performing these actions using your blood, which increases to +2 if you're a master in Medicine and +3 if you're legendary.

**Source:** `= this.source` (`= this.source-type`)
