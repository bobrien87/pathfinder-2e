---
type: background
source-type: "Remaster"
boosts: "Int/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Guild Lore Lore"
feats: "[[Specialty Crafting]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

As an apprentice, you practiced a particular form of building or crafting, developing a specialized skill. You might have been a blacksmith's apprentice toiling over the forge for countless hours, a young tailor sewing garments of all kinds, or a shipwright shaping the hulls of ships.

Choose two attribute boosts. One must be to **Strength** or **Intelligence**, and one is a free attribute boost.

You're trained in the Crafting skill and the Guild Lore skill. You gain the [[Specialty Crafting]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
