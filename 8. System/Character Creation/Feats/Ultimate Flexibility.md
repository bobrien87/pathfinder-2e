---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Fighter]]"]
prerequisites: "improved flexibility"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your experience keeps you on your toes, helping you adopt complex strategies on the fly and face the most dangerous challenges. When you gain a fighter feat using combat flexibility, you gain three fighter feats instead of two. While the first feat must still be 8th level or lower, the second feat can be up to 14th level, and the third feat can be up to 18th level.

You can use the first feat to meet the prerequisites of the second or third feats and the second feat to meet the prerequisites of the third feat. You must meet all three feats' other prerequisites normally.

In addition, you can adapt to the battlefield's challenges by spending 1 hour to train. If you do, you can reselect the feats chosen with combat flexibility as if you had made your daily preparations. You can't trade out limited-use abilities that you've already used, such as Determination.

**Source:** `= this.source` (`= this.source-type`)
