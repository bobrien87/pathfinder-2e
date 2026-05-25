---
type: background
source-type: "Remaster"
boosts: "Dex/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Cooking Lore Lore"
feats: "[[Seasoned]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're an inspired chef, trying to make it as big as you can out on the open road. You travel with a wood or iron cart that doubles as your portable business and shelter. Struggling for funds or fighting for a place to set up shop are common plights in your daily life. However, there's no one hungrier than a budding adventurer, and you're very affordable, always there with the perfect meal.

Choose two attribute boosts. One must be to **Strength** or **Dexterity**, and one is a free attribute boost.

You're trained in either Crafting or Society, and Cooking Lore. You gain the Seasoned skill feat.

**Source:** `= this.source` (`= this.source-type`)
