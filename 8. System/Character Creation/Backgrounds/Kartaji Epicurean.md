---
type: background
source-type: "Remaster"
boosts: "Con/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Cooking Lore Lore"
feats: "[[Additional Lore]]"
source: "Pathfinder Myth-Speaker Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Each city-state hides enough secrets to occupy an adventurer for a lifetime. Even so, many seek the varied experiences and sites at each of Iblydos's eminent cities. You have toured much of Kardaji Bay and the Iblydan archipelago, be that as a trader, an envoy, or a tourist. Along the way, you've incorporated local idioms, idiosyncrasies, and ingredients into your cosmopolitan lifestyle. You've most recently reached Bailax, ready for new adventures.

Choose two attribute boosts. One must be to **Constitution** or **Intelligence**, and one is a free attribute boost.

You're trained in either the Crafting or Society skill and the Cooking Lore skill. You gain the [[Additional Lore]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
