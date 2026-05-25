---
type: background
source-type: "Remaster"
boosts: "Con/Str, Cha/Con/Dex/Int/Str/Wis"
skills: "Athletics, Labor Lore Lore"
feats: "[[Hefty Hauler]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.boosts != null and this.boosts != "", "**Attribute Boosts** " + this.boosts, "") + choice(this.skills != null and this.skills != "", choice(this.boosts != null and this.boosts != "", "<br>", "") + "**Trained Skill** " + this.skills, "") + choice(this.feats != null and this.feats != "", choice(this.boosts != null and this.boosts != "" or this.skills != null and this.skills != "", "<br>", "") + "**Gained Feat** " + this.feats, "")`

You've spent years performing arduous physical labor. It was a difficult life, but you somehow survived. You may have embraced adventuring as an easier method to make your way in the world, or you might adventure under someone else's command.

Choose two attribute boosts. One must be to **Strength** or **Constitution**, and one is a free attribute boost.

You're trained in the Athletics skill and the Labor Lore skill. You gain the [[Hefty Hauler]] skill feat.

**Source:** `= this.source` (`= this.source-type`)
