---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Nature, Stabling Lore Lore"
feats: "[[Express Rider]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

During times of war, armies might venture far from the seats of government that send them out or get separated from their commanders by the terrain. Thanks to your riding skill and affinity with the animals that serve as mounts, you were tasked with carrying reports of an ongoing war from one place to another. Speed was of utmost importance, and sometimes you would need to spend days in the saddle.

Choose two attribute boosts. One must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Nature skill and the Stabling Lore skill. You gain the [[Express Rider]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
