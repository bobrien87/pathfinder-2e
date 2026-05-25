---
type: background
source-type: "Remaster"
boosts: "Cha/Int, Cha/Con/Dex/Int/Str/Wis"
skills: "Society, Scribing Lore Lore"
feats: "[[Multilingual]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

Keeping your finger on the pulse of the city, you write a small news broadsheet to sell on street corners. You rent the use of a printing press to achieve this goal, so you're familiar with such machines. However, people and their stories are your main focus, and you adventure to chase the latest scoop.

Choose two attribute boosts. One must be to **Intelligence** or **Charisma**, and one is a free attribute boost.

You're trained in the Society skill and the Scribing Lore skill. You gain the [[Multilingual]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
