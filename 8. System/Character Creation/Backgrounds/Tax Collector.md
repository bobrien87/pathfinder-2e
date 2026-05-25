---
type: background
source-type: "Remaster"
boosts: "Cha/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Intimidation"
feats: "[[Quick Coercion]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Reviled but required, you were sent when taxes were due. Performing your job might have required travel and persuasion, or perhaps you were responsible for collecting taxes on trade. Either way, it sometimes meant dirty hands, and adventuring seemed the next logical step to you.

Choose two attribute boosts. One must be to **Strength** or **Charisma**, and one is a free attribute boost.

You're trained in the Intimidation skill and the Lore skill for the settlement that employed you. You gain the [[Quick Coercion]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
