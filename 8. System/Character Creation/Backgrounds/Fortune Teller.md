---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Occultism, Fortune-Telling Lore Lore"
feats: "[[Oddity Identification]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

The strands of fate are clear to you, as you have learned many traditional forms by which laypeople can divine the future. You might have used these skills to guide your community, or simply to make money. But even the slightest peek into these practices connects you to the occult mysteries of the universe.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in the Occultism skill and the Fortune-Telling Lore skill. You gain the [[Oddity Identification]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
