---
type: background
source-type: "Remaster"
boosts: "Cha/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Art Lore Lore"
feats: "[[Specialty Crafting]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Your art is your greatest passion, whatever form it takes. Adventuring might help you find inspiration, or simply be a way to survive until you become a world-famous artist.

Choose two attribute boosts. One must be to **Dexterity** or **Charisma**, and one is a free attribute boost.

You're trained in the Crafting skill and the Art Lore skill. You gain the [[Specialty Crafting]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
