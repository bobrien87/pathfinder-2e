---
type: background
source-type: "Remaster"
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Intimidation, Hunting Lore Lore"
feats: "[[Group Coercion]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You hold an official title of sheriff or deputy in a small community. Those that would do harm to others flee your gaze, for they know it brings the promise of castigation. You protect your town, watch over those who have placed their trust in you, and make sure those that would do others harm are brought to justice.

Choose two attribute boosts. One must be to **Dexterity** or **Charisma**, and one is a free attribute boost.

You're trained in the Intimidation skill and the Hunting Lore skill. You gain the [[Group Coercion]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
