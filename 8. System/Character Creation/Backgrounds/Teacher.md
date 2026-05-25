---
type: background
source-type: "Remaster"
boosts: "Int/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Academia Lore Lore"
feats: "[[Experienced Professional]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You are incredibly knowledgeable, skilled, and perhaps even trained to teach children and adults about the world and its wonders. From books to classes, you're committed to imparting knowledge to all. Not everything can be taught or learned from a book, though, so you've become an adventurer to learn subjects more directly and bring that wisdom back to your students.

Choose two attribute boosts. One must be to **Intelligence** or **Wisdom**, and one is a free attribute boost.

You're trained in your choice of either the Performance or Society skill, as well as the Academia Lore skill. You gain the [[Experienced Professional]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
