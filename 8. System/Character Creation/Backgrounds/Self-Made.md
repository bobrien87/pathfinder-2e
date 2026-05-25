---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics"
feats: "[[Hefty Hauler]]"
source: "Pathfinder Triumph of The Tusk Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Some are born with everything they need in this life, but not you—you scraped everything you have together through hard work and sheer force of will. You might have done hard manual labor to get where you are or apprenticed for years to become a master of your craft.

Choose two attribute boosts. One must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Athletics skill and a Lore skill related to how you've paved your own way through the world. You gain the [[Hefty Hauler]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
