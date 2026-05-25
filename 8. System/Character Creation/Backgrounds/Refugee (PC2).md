---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Society"
feats: "[[Streetwise]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You come from a land very distant from the one you now find yourself in, driven by war, plague, or simply in the pursuit of opportunity. Regardless of your origin or the reason you left your home, you find yourself an outsider in this new land. Adventuring is a way to support yourself while offering hope to those who need it most.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Society skill and a Lore skill related to the settlement you came from. You gain the [[Streetwise]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
