---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Engineering Lore Lore"
feats: "[[Specialty Crafting]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Creating all sorts of minor inventions scratches your itch for problem-solving. Your engineering skills take a particularly creative bent, and no one know what you'll come up with next. It might be a genius device with tremendous potential or it might explode.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Crafting skill and the Engineering Lore skill. You gain the [[Specialty Crafting]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
