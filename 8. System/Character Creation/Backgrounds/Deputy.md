---
type: background
source-type: "Remaster"
boosts: "Dex/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Hunting Lore Lore"
feats: "[[Experienced Tracker]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

While your life may have taken some twists and turns in the intervening years, you were once deputized as the lawful protector of a community. While the role was temporary and you've since turned in your badge, that responsibility shaped you. Whenever a community is in trouble, and the sheriff is nowhere to be found, residents call on you to capture a criminal, rescue the mayor's offspring from bandits, or go toe to toe with outlaws.

Choose two attribute boosts. One must be to **Dexterity** or **Wisdom**, and one is a free attribute boost.

You're trained in the Survival skill and the Hunting Lore skill. You gain the [[Experienced Tracker]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
