---
type: background
source-type: "Remaster"
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Thievery, Engineering Lore Lore"
feats: "[[Concealing Legerdemain]]"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Your introduction to the criminal life was spurred forward by a seemingly innocuous hammer that provided you with all kinds of innovative criminal ideas. It has since left your possession, but every now and then you hear a faint whisper urging you toward crime.

Choose two attribute boosts. One must be to **Dexterity** or **Charisma**, and one is a free attribute boost.

You're trained in the Thievery skill and Engineering Lore. You gain the [[Concealing Legerdemain]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
