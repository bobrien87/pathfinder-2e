---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Mining Lore Lore"
feats: "[[Terrain Expertise]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You earned a living wrenching precious minerals from the lightless depths of the earth. Adventuring might have seemed lucrative or glamorous compared to this backbreaking labor—and if you have to head back underground, this time you plan to do so armed with a real weapon instead of a miner's pick.

Choose two attribute boosts. One must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Survival skill and the Mining Lore skill. You gain the [[Terrain Expertise]] skill feat with underground terrain.

**Source:** `= this.source` (`= this.source-type`)
