---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Warfare Lore Lore"
feats: "[[Armor Assist]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have seen more battles than you can remember and have managed to make it through them mostly intact. Nothing surprises you anymore, except maybe when things actually go as planned. You are always pleasantly surprised when you manage to survive another day.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Athletics skill and the Warfare Lore skill. You gain the [[Armor Assist]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
