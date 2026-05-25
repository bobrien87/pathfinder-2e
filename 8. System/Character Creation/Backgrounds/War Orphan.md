---
type: background
source-type: "Remaster"
boosts: "Con/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Thievery, Underworld Lore Lore"
feats: "[[Dirty Trick]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The horrors of war have left you orphaned and alone, forcing you to fend for yourself until you were taught the ways of the world by a group of similarly affected youths. They were like a new family to you, but you had to live outside the law in order to survive. Those days are behind you now, but there are certain tricks you'll never forget.

Choose two attribute boosts. One must be to **Dexterity** or **Constitution**, and one is a free attribute boost.

You're trained in the Thievery skill and the Underworld Lore skill. You gain the [[Dirty Trick]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
