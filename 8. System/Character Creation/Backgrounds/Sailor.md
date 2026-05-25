---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Sailing Lore Lore"
feats: "[[Underwater Marauder]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You heard the call of the sea from a young age. Perhaps you signed onto a merchant's vessel, joined the navy, or even fell in with a crew of pirates and scalawags.

Choose two attribute boosts. One must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in the Athletics skill and the Sailing Lore skill. You gain the [[Underwater Marauder]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
