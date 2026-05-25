---
type: background
source-type: "Remaster"
boosts: "Str/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Survival, Scouting Lore Lore"
feats: "[[Survey Wildlife]]"
source: "Pathfinder Wardens of Wildwood Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

For all their thorns, beasts, and hazards, the wilds aren't invulnerable. If the natural wonders of the Verduran Forest are to survive, they need guardians like you. You have learned to monitor and protect wildernesses, earning you the Verduran Lodge's respect even if you're not affiliated with any druidic organization. Perhaps you grew up in a community that revered and carefully managed its local ecosystem, learning millennia-old traditions. It could be you were an unlikely survivor who learned to live off the land out of necessity, gradually becoming its protector. Whatever the case, traveling to the Greenwood Gala is a great opportunity to share your knowledge, learn new tricks, and recruit allies who can help defend your home.

Choose two attribute boosts. One must be to **Strength** or **Wisdom**, and one is a free attribute boost.

You're trained in the Survival skill and the Scouting Lore skill. You gain the [[Survey Wildlife]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
