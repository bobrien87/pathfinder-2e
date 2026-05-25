---
type: background
source-type: "Remaster"
boosts: "Dex/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Crafting, Engineering Lore Lore"
feats: "[[Quick Repair]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

From a young age, you apprenticed to an experienced gunsmith and over time your skill and knowledge rose to match that of your master. Today, you can easily repair, modify, or improve nearly any firearm you've seen before, and even if you haven't seen it, you'll break it down to learn about what makes it tick in no time. You've taken those skills on the road, using them to assist yourself and your allies as an adventurer when it comes to maintaining their weapons, shields, armor, and more.

Choose two attribute boosts. One of these boosts must be to **Intelligence** or **Dexterity**, and one is a free attribute boost.

You're trained in the Crafting skill and the Engineering Lore skill. You gain the [[Quick Repair]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
