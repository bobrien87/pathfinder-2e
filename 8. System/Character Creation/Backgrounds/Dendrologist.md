---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Plane of Wood Lore Lore"
feats: "[[Terrain Expertise]]"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Trees grow in every biome, and your awe at their ability to conquer terrain has inspired deeper study into their workings. There are trees everywhere, and your study of them will inevitably take you ever further afield in search of new varieties, perhaps even to the Plane of Wood itself.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in the Survival skill and the Plane of Wood Lore skill. You gain the [[Terrain Expertise]] skill feat for forests.

**Source:** `= this.source` (`= this.source-type`)
