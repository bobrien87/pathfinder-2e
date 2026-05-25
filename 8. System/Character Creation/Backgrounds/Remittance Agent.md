---
type: background
source-type: "Remaster"
boosts: "Con/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society"
feats: "[[Experienced Professional]]"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

When money, goods, or merchandise need to be moved over great distances, remittance agents are better and more trustworthy than your local mercenary. You know the ins and outs of trading routes and the protocols that come with them. While some might consider you a standard adventurer or mercenary, you know you can get the job done better and safer than anyone else.

Choose two attribute boosts. One must be to **Constitution** or **Intelligence**, and one is a free attribute boost.

You're trained in Society, and either Labor Lore or Mercenary Lore. You gain the Experienced Professional skill feat.

**Source:** `= this.source` (`= this.source-type`)
