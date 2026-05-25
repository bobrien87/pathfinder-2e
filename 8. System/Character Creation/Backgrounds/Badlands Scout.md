---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Badlands Lore Lore"
feats: "[[Forager]]"
source: "Pathfinder Triumph of The Tusk Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You're accustomed to the desolate wilds of Belkzen and able to blend into the sparse shadows of craggy rocks and quench your thirst with drops of water. You might be a member of an isolated orc hold, traveling mercenary, or wandering warrior from nearby human settlements.

Choose two attribute boosts. One must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Survival skill and the Badlands Lore skill. You gain the [[Forager]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
