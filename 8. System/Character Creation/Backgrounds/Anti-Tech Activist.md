---
type: background
source-type: "Remaster"
boosts: "Cha/Con, Cha/Con/Dex/Int/Str/Wis"
skills: "Intimidation, Guild Lore Lore"
feats: "[[Group Coercion]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You've seen the sorts of things that technology brings—polluted environments, workers put out of their jobs or horribly injured, and the slow erosion of society—and you've vowed to inform the larger world of these ills. You do so with long, impassioned speeches on street corners and village squares and by talking personally with the heads of various guilds. Adventuring into the wider world could help spread your message even farther.

Choose two attribute boosts. One must be to **Constitution** or **Charisma**, and one is a free attribute boost.

You're trained in the Intimidation skill and the Guild Lore skill. You gain the [[Group Coercion]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
