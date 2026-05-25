---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Thievery, Engineering Lore Lore"
feats: "[[Concealing Legerdemain]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Whether you do it for personal enjoyment or at the behest of a mercenary company or military organization, you have a knack for destroying things. You have a sense for an object or structure's weak spots and know where to deliver a hammer strike or alchemical bomb. You adventure to hone your skills or complete a particular mission.

Choose two attribute boosts. One must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in the Thievery skill and the Engineering Lore skill. You gain the [[Concealing Legerdemain]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
