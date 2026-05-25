---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Gem Lore Lore"
feats: "[[Crafter's Appraisal]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

As an artisan by trade, your materials of choice are precious metals and stones. You're a trained jeweler with an eye for structure and beauty. Your designs reflect your creativity and years of training. Maybe you mastered your craft through trial and error, or perhaps this trade was passed down to you through your family. Regardless of how you acquired your skills, you've sought the life of an adventurer.

Choose two attribute boosts. One must be to **Wisdom** or **Intelligence**, and one is a free attribute boost.

You're trained in Crafting and Gem Lore. You gain the Crafter's Appraisal skill feat.

**Source:** `= this.source` (`= this.source-type`)
