---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Orc Pantheon Lore Lore"
feats: "[[Multilingual]]"
source: "Pathfinder Triumph of The Tusk Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Belkzen has a long, storied history, but much of it has been erased by time, conflict, and the deliberate cruelty of those who wished to destroy records of the past. You have dedicated your studies to collecting the fragmented stories of Belkzen's past so you can weave together a full picture of the land's lost cultures and knowledge, that the nation might be remembered properly by the world.

Choose two attribute boosts. One must be to **Dexterity** or **Intelligence**, and one is a free attribute boost.

You're trained in the Society skill and the Orc Pantheon Lore skill, a broad skill pertaining to orc gods both current and past. You gain the [[Multilingual]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
