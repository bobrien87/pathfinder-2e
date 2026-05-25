---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Engineering Lore Lore"
feats: "[[Streetwise]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You came to Alkenstar because you heard they had guns, but you stayed because of the atmosphere. Or the guns. Either way, journalism and scientific curiosity opened the door to a life of adventure. Now you continue to adventure in the Alkenstar area, using your skills to deal with whatever situations present themselves.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in Society and Engineering Lore. You gain the [[Streetwise]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
