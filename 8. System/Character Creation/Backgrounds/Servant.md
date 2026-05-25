---
type: background
source-type: "Remaster"
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Labor Lore Lore"
feats: "[[Read Lips]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You held a role of servitude, waiting on nobles and engendering their trust as one of the confidantes of the household. You might have walked away on good terms, or perhaps you know dangerous secrets about your former employers. Regardless, you're adventuring for a change and finding that in this new role, the skills you've learned now serve you.

Choose two attribute boosts. One must be to **Dexterity** or **Charisma**, and one is a free attribute boost.

You're trained in the Society skill and the Labor Lore skill. You gain the [[Read Lips]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
