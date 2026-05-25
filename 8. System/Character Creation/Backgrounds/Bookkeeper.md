---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Accounting Lore Lore"
feats: "[[Eye For Numbers]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You ran the numbers on a large farm, for a merchant's endeavors, or with a major guild in the city. You kept track of expenses, payroll, profits, and anything else that had to do with money, for better or worse. If better, you might be adventuring to learn how others ply this trade. If worse, you may be fleeing from impending consequences in the hope that no one finds you.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Society skill and the Accounting Lore skill. You gain the [[Eye for Numbers]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
