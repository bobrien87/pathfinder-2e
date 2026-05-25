---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Cooking Lore Lore"
feats: "[[Forager]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

**Access** Tian Xia origin

With plenty of time to hone your culinary skill, you can make the most out of any dish you create. You have much experience with using the most difficult and hardiest of ingredients, as Zi Ha is known for housing many carnivorous plants, toxic fungi, and hardy, woolly animals. There are many reasons why a seasoned chef like you would seek adventure, whether to expand your palette or to explore other countries' cuisines.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in Survival and Cooking Lore. You gain the Forager skill feat.

**Source:** `= this.source` (`= this.source-type`)
