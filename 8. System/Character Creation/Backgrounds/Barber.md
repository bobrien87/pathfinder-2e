---
type: background
source-type: "Remaster"
boosts: "Dex/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Medicine, Surgery Lore Lore"
feats: "[[Risky Surgery]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Haircuts, dentistry, bloodletting, and surgery—if it takes a steady hand and a razor, you can do it. You may have taken to the road to expand your skills or test yourself against a world that leaves your patients so battered and bruised.

Choose two attribute boosts. One must be to **Dexterity** or **Wisdom**, and one is a free attribute boost.

You're trained in the Medicine skill and the Surgery Lore skill. You gain the [[Risky Surgery]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
