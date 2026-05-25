---
type: background
source-type: "Remaster"
boosts: "Cha/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy, Lore skill pertaining to your place of origin Lore"
feats: "[[No Cause for Alarm]]"
source: "Pathfinder Hellbreakers Player’s Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You hail from another nation, fighting a battle that isn't your own. You might be an agent from Andoran with sympathies for the locals or a hired hand from the Druma Mercenary League. Regardless of how or why, you're here now, and your duty is to do what you can to help those you find yourself in league with.

Choose two attribute boosts. One must be to **Charisma** or **Strength**, and one is a free attribute boost.

You're trained in the Diplomacy skill and a Lore skill pertaining to your place of origin. You gain the [[No Cause for Alarm]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
