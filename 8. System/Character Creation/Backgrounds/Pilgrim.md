---
type: background
source-type: "Remaster"
boosts: "Cha/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Religion"
feats: "[[Pilgrim's Token]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

In your youth, you made several pilgrimages to important shrines and sacred sites. You might have been a mendicant friar, a seller of religious relics (real or fraudulent), or just a simple farmer following the dictates of your faith. Whatever the aims of your wanderings now, your faith still protects you on the road.

Choose two attribute boosts. One must be to **Wisdom** or **Charisma**, and one is a free attribute boost.

You're trained in the Religion skill and the Lore skill for your patron deity. You gain the [[Pilgrim's Token]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
