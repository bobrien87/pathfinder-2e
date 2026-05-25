---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Engineering Lore Lore"
feats: "[[Crafter's Appraisal]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

New forms of clockwork technology are incredibly interesting to you, and you've been studying examples of them to see where else they might be best put to use. You might eventually develop a new prototype machine or find a way to make related technologies practical enough for everyone to benefit. Though before you do, you must continue your research!

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Society skill and the Engineering Lore skill. You gain the [[Crafter's Appraisal]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
