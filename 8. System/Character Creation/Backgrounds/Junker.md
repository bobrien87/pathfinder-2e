---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics"
feats: "[[Hefty Hauler]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You live on the outskirts of civilization, combing through the detritus left behind for interesting trinkets to sell or use in your own crafting. Though you have a preferred terrain to search, you know that the greatest treasures occur where people make greater use of technology.

Choose two attribute boosts. One must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Athletics skill and the Lore skill of the terrain in which you scavenge. You gain the [[Hefty Hauler]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
