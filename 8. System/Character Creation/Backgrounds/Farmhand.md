---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Farming Lore Lore"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

With a strong back and an understanding of seasonal cycles, you tilled the land and tended crops. Your farm could have been razed by invaders, you could have lost the family tying you to the land, or you might have simply tired of the drudgery, but at some point, you became an adventurer.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Athletics skill and the Farming Lore skill. You gain the [[Assurance]] skill feat with Athletics.

**Source:** `= this.source` (`= this.source-type`)
