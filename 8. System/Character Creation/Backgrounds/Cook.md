---
type: background
source-type: "Remaster"
boosts: "Con/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Cooking Lore Lore"
feats: "[[Seasoned]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You grew up in the kitchens of a tavern or other dining establishment and excelled there, becoming an exceptional cook. Baking, cooking, a little brewing on the side—you've spent lots of time out of sight. It's about time you went out into the world to catch some sights for yourself.

Choose two attribute boosts. One must be to **Constitution** or **Intelligence**, and one is a free attribute boost.

You're trained in the Survival skill and the Cooking Lore skill. You gain the [[Seasoned]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
