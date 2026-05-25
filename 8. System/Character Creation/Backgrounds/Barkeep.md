---
type: background
source-type: "Remaster"
boosts: "Cha/Con, Cha/Con/Dex/Int/Str/Wis"
skills: "Diplomacy, Alcohol Lore Lore"
feats: "[[Hobnobber]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have five specialties: hefting barrels, drinking, polishing steins, drinking, and drinking. You worked in a bar, where you learned how to hold your liquor and rowdily socialize.

Choose two attribute boosts. One must be to **Constitution** or **Charisma**, and one is a free attribute boost.

You're trained in the Diplomacy skill and the Alcohol Lore skill. You gain the [[Hobnobber]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
