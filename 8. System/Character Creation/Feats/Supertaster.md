---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]"]
prerequisites: "master in Perception"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have refined your palate and have a discerning sense of taste that can detect abnormalities in the flavor and texture of food and beverages. When eating food or drinking a beverage, you automatically attempt to identify the ingredients, which might alert you to the presence of alterations or additives, such as poisons. The GM rolls a secret Perception check against a DC determined by the poison's level; if the food or drink is poisoned, on a success, you learn that the food or drink was poisoned, but not the specific poison used. If you successfully detect that the food or drink was poisoned, you can spit out the food or drink in time to not be exposed to that instance of the poison (unless you resume eating or drinking the poisoned food or beverage).

If you lick or taste something while Investigating or attempting to Recall Knowledge to identify something, and if the taste would provide relevant additional information (at the GM's discretion), you gain a +2 circumstance bonus to your check.

**Source:** `= this.source` (`= this.source-type`)
