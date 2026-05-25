---
type: background
source-type: "Remaster"
boosts: "Con/Dex, Cha/Con/Dex/Int/Str/Wis"
skills: "Thievery, Underworld Lore Lore"
feats: "[[Subtle Theft]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're an outlaw whose first crime was stealing the guns from Alkenstar's Gunworks which allowed you to commence a crime spree of epic proportions. You don't know where your road ends, but it's probably going to be a bloody affair. The life of an adventurer might even be a relief compared to a life forever on the run from Alkenstar authorities and their allies.

Choose two attribute boosts. One boost must be to **Dexterity** or **Constitution**, and one is a free attribute boost.

You're trained in Thievery and Underworld Lore. You gain the [[Subtle Theft]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
