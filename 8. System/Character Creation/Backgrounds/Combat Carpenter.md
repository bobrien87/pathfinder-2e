---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Engineering Lore Lore"
feats: "[[Specialty Crafting]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have spent countless hours selecting lumber, drafting designs, and constructing all manner of wooden buildings, shields, weapons, and tools. You can readily identify the weak spots in wooden fortifications and determine the best ways to bolster or attack them.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Crafting skill and the Engineering Lore skill. You gain the [[Specialty Crafting]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
