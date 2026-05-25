---
type: background
source-type: "Remaster"
boosts: "Con/Wis, Cha/Con/Dex/Int/Str/Wis"
skills: "Religion"
feats: "[[Pilgrim's Token]]"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

While you once spoke to a small congregation in a ramshackle church, those days are behind you now. Your church was destroyed, your congregants scattered, and now you meander the lands holding a worn copy of your religious text in one hand, and a fiery conviction in the other.

Choose two attribute boosts. One boost must be to **Constitution** or **Wisdom**, and one is a free attribute boost.

You're trained in the Religion skill and a Lore skill associated with the deity you preach for (such as Pharasmin Lore). You gain the [[Pilgrim's Token]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
