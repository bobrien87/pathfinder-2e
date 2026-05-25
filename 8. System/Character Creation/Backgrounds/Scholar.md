---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Academia Lore Lore"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You have a knack for learning and sequestered yourself from the outside world to learn all you could. You read about so many wondrous places and things in your books, always dreaming about one day seeing the real things. Eventually, that curiosity led you to leave your studies and become an adventurer.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in your choice of the Arcana, Nature, Occultism, or Religion skill, and gain the [[Assurance]] skill feat in your chosen skill. You're also trained in the Academia Lore skill.

**Source:** `= this.source` (`= this.source-type`)
