---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Exemplar]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

While tales of your divine ikons have spread far and wide, you've realized that, as they are all manifestations of your soul, the object itself is unnecessary. Your ikons disintegrate into golden light. Any ikon feats you've taken now apply to any applicable ikon you have, not just one, and you can immediately retrain any ikon feats you selected more than once.

Each day during your daily preparations, you can select one ikon feat of 16th level or lower and gain it temporarily for that day. You can place your divine spark into any object in your possession, even a nonthreatening object like a single strand of grass, to transform it into a fully functional copy of your ikon made out of pure divine radiance. You can do this as a free action immediately before or after Striking with or otherwise using the ikon.

**Source:** `= this.source` (`= this.source-type`)
