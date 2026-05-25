---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Nature, Green Faith Lore Lore"
feats: "[[Natural Medicine]]"
source: "Pathfinder Wardens of Wildwood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You are an adherent of the Green Faith, striving to bring harmony between nature and civilization. While you might hail from Shining Kingdom region surrounding the Verduran Forest, the annual Moot of Ages draws visitors from across the world. Traveling here is a sacred journey that could deepen your understanding of nature's will. As part of your journey and natural communion, you've relied heavily on flora and fauna to ease your sores and other injuries.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Nature skill and the Green Faith Lore skill. You gain the [[Natural Medicine]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
