---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Tanuki]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

While walking down the road on a moonlit night, one might be puzzled to find a shop or hill that wasn't there before. In reality, this is a tanuki at the height of their power. When you Change Shape, you can transform into a building or terrain feature up to 50 feet tall and up to 50 feet on a side. Mundane features of your landscape form function as normal—for instance, if you transform into a hot spring, the hot spring contains relaxing hot water, and if you transform into an inn, the inn contains bedrooms, beds, and delicious food—though no aspect of your landscape form can be an active hazard that can cause damage or impose conditions, and any objects created within your landscape form turn into leaves if taken outside of it. You can speak while in landscape form, but you can't attack, cast spells, or move. You can remain in landscape form for up to 8 hours, and when you exit landscape form, it dissolves around anyone who was inside of it.

**Source:** `= this.source` (`= this.source-type`)
